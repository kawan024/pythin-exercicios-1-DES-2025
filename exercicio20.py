if (senhaDigitada.equals(senha)) {
        System.out.println("Acesso permitido!");
    }
    while (!senha.equals(senhaDigitada)) {
        System.out.println("Acesso negado!");
        System.out.println("Tente novamente: ");
        String tentativa = scanner.next();

        if (tentativa.equals(senha)) {
            System.out.println("Acesso permitido!");
            break;
        }
    }
}
#finalidade