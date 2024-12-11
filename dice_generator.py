from PIL import Image, ImageDraw

def create_dice_image(number, size=60):
    # Criar uma nova imagem com fundo branco
    image = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(image)
    
    # Desenhar borda do dado
    draw.rectangle([(0, 0), (size-1, size-1)], outline='black')
    
    # Tamanho e posições dos pontos
    dot_size = size // 10
    positions = {
        1: [(size//2, size//2)],
        2: [(size//4, size//4), (3*size//4, 3*size//4)],
        3: [(size//4, size//4), (size//2, size//2), (3*size//4, 3*size//4)],
        4: [(size//4, size//4), (3*size//4, size//4),
            (size//4, 3*size//4), (3*size//4, 3*size//4)],
        5: [(size//4, size//4), (3*size//4, size//4),
            (size//2, size//2),
            (size//4, 3*size//4), (3*size//4, 3*size//4)],
        6: [(size//4, size//4), (3*size//4, size//4),
            (size//4, size//2), (3*size//4, size//2),
            (size//4, 3*size//4), (3*size//4, 3*size//4)]
    }
    
    # Desenhar os pontos
    for x, y in positions[number]:
        draw.ellipse([(x-dot_size, y-dot_size), 
                     (x+dot_size, y+dot_size)], 
                    fill='black')
    
    return image

def generate_dice_images():
    # Criar imagens para cada número do dado
    for i in range(1, 7):
        dice = create_dice_image(i)
        dice.save(f'dice_images/dice_{i}.png')

if __name__ == "__main__":
    import os
    if not os.path.exists('dice_images'):
        os.makedirs('dice_images')
    generate_dice_images()
