import java.util.Scanner;

public class ValidacaoInformacoes {
    private static boolean validarNome(String nome) {
        return nome.length() > 3;
    }

    private static boolean validarIdade(int idade) {
        return idade >= 0 && idade <= 150;
    }

    private static boolean validarSalario(double salario) {
        return salario > 0;
    }

    private static boolean validarSexo(char sexo) {
        return sexo == 'M' || sexo == 'F' || sexo == 'm' || sexo == 'f';
    }

    private static boolean validarEstadoCivil(char estadoCivil) {
        char estado = Character.toUpperCase(estadoCivil);
        return estado == 'S' || estado == 'C' || estado == 'V' || estado == 'D';
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String nome;
        int idade;
        double salario;
        char sexo, estadoCivil;

        // Validação do nome
        do {
            System.out.print("Digite o nome (mais que 3 caracteres): ");
            nome = scanner.nextLine();
            if (!validarNome(nome)) {
                System.out.println("Nome inválido! Deve ter mais que 3 caracteres.");
            }
        } while (!validarNome(nome));

        // Validação da idade
        do {
            System.out.print("Digite a idade (entre 0 e 150): ");
            idade = scanner.nextInt();
            if (!validarIdade(idade)) {
                System.out.println("Idade inválida! Deve estar entre 0 e 150.");
            }
        } while (!validarIdade(idade));

        // Validação do salário
        do {
            System.out.print("Digite o salário (maior que zero): ");
            salario = scanner.nextDouble();
            if (!validarSalario(salario)) {
                System.out.println("Salário inválido! Deve ser maior que zero.");
            }
        } while (!validarSalario(salario));

        // Validação do sexo
        do {
            System.out.print("Digite o sexo (M/F): ");
            sexo = scanner.next().charAt(0);
            if (!validarSexo(sexo)) {
                System.out.println("Sexo inválido! Digite M ou F.");
            }
        } while (!validarSexo(sexo));

        // Validação do estado civil
        do {
            System.out.print("Digite o estado civil (S/C/V/D): ");
            estadoCivil = scanner.next().charAt(0);
            if (!validarEstadoCivil(estadoCivil)) {
                System.out.println("Estado civil inválido! Digite S, C, V ou D.");
            }
        } while (!validarEstadoCivil(estadoCivil));

        System.out.println("\nInformações validadas com sucesso!");
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Salário: " + salario);
        System.out.println("Sexo: " + sexo);
        System.out.println("Estado Civil: " + estadoCivil);

        scanner.close();
    }
}
