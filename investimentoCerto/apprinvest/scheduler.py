from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone
from .models import FinancialIndicator, NewsArticle, APILog
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def update_financial_indicators():
    """Atualiza indicadores financeiros usando a API do Yahoo Finance"""
    symbols = [
        '^BVSP',  # Ibovespa
        'BRL=X',  # USD/BRL
        'GC=F',   # Gold Futures
        '^TNX',   # Treasury Yield 10 Years
        'BTC-USD' # Bitcoin
    ]
    
    try:
        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            
            indicator, created = FinancialIndicator.objects.get_or_create(
                symbol=symbol,
                defaults={'name': info.get('longName', symbol)}
            )
            
            indicator.current_value = info.get('regularMarketPrice', 0)
            indicator.variation = info.get('regularMarketChangePercent', 0)
            indicator.last_update = timezone.now()
            indicator.source = 'Yahoo Finance'
            indicator.save()
            
            APILog.objects.create(
                level='INFO',
                source='Yahoo Finance',
                message=f'Indicador {symbol} atualizado com sucesso',
                details={'price': str(indicator.current_value), 'variation': str(indicator.variation)}
            )
            
    except Exception as e:
        APILog.objects.create(
            level='ERROR',
            source='Yahoo Finance',
            message=f'Erro ao atualizar indicadores: {str(e)}',
            details={'error': str(e)}
        )
        logger.error(f'Erro ao atualizar indicadores: {str(e)}')

def fetch_financial_news():
    """Busca notícias financeiras de fontes confiáveis"""
    sources = [
        {
            'name': 'Valor Econômico',
            'url': 'https://valor.globo.com/financas/rss',
            'type': 'rss'
        },
        {
            'name': 'InfoMoney',
            'url': 'https://www.infomoney.com.br/feed/',
            'type': 'rss'
        },
        {
            'name': 'Reuters Brasil',
            'url': 'https://www.reuters.com/news/rss/brazil',
            'type': 'rss'
        }
    ]
    
    try:
        for source in sources:
            response = requests.get(source['url'])
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'xml')
                items = soup.find_all('item')
                
                for item in items[:10]:
                    title = item.title.text
                    link = item.link.text
                    description = item.description.text
                    pub_date = timezone.datetime.strptime(
                        item.pubDate.text,
                        '%a, %d %b %Y %H:%M:%S %z'
                    )
                    
                    NewsArticle.objects.update_or_create(
                        source_url=link,
                        defaults={
                            'title': title,
                            'summary': description,
                            'content': description,
                            'source_name': source['name'],
                            'published_date': pub_date,
                            'is_verified': True
                        }
                    )
                
                APILog.objects.create(
                    level='INFO',
                    source=source['name'],
                    message=f'Notícias atualizadas com sucesso',
                    details={'count': len(items)}
                )
                
    except Exception as e:
        APILog.objects.create(
            level='ERROR',
            source='News Fetcher',
            message=f'Erro ao buscar notícias: {str(e)}',
            details={'error': str(e)}
        )
        logger.error(f'Erro ao buscar notícias: {str(e)}')

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    # Agenda a atualização dos indicadores financeiros a cada 5 minutos
    scheduler.add_job(
        update_financial_indicators,
        'interval',
        minutes=5,
        name='update_indicators',
        jobstore='default',
        id='update_indicators',
        replace_existing=True
    )
    
    # Agenda a busca de notícias a cada 15 minutos
    scheduler.add_job(
        fetch_financial_news,
        'interval',
        minutes=15,
        name='fetch_news',
        jobstore='default',
        id='fetch_news',
        replace_existing=True
    )
    
    scheduler.start()
