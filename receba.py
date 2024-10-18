class Estoque:
    def __init__(self, estoque_inicial):
        self.produtos = {
            'ovo': estoque_inicial[0],      
            'Dolly': estoque_inicial[1],   
            'carne': estoque_inicial[2], 
            'nescau': estoque_inicial[3],   
            'arroz': estoque_inicial[4]      
        }

    def adicionar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome] += quantidade
            print(f'Produto "{nome}" adicionado. Quantidade atual: {self.produtos[nome]}')
        else:
            print(f'Erro: Produto "{nome}" não encontrado no estoque.')

    def vender_produto(self, nome, quantidade):
        if nome in self.produtos and self.produtos[nome] >= quantidade:
            self.produtos[nome] -= quantidade
            print(f'Produto "{nome}" vendido. Quantidade restante: {self.produtos[nome]}')
        else:
            print(f'Não é possível vender "{nome}". Estoque insuficiente ou produto não encontrado.')

    def mostrar_estoque(self):
        if not self.produtos:
            print("O estoque está vazio.")
        else:
            print("Estoque atual:")
            for nome, quantidade in self.produtos.items():
                print(f'- {nome}: {quantidade}')


def main():
    estoque_inicial = [20, 15, 10, 30, 5]
    estoque = Estoque(estoque_inicial)

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar quantidade ao produto")
        print("2. Vender produto")
        print("3. Mostrar estoque")
        print("4. Sair")
        
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("\nProdutos existentes no estoque:")
            for produto in estoque.produtos.keys():
                print(f"- {produto}")
            nome = input("Digite o nome do produto: ").lower()
            quantidade = int(input("Digite a quantidade a ser adicionada: "))
            estoque.adicionar_produto(nome, quantidade)
        elif opcao == '2':
            nome = input("Digite o nome do produto: ").lower()
            quantidade = int(input("Digite a quantidade a ser vendida: "))
            estoque.vender_produto(nome, quantidade)
        elif opcao == '3':
            estoque.mostrar_estoque()
        elif opcao == '4':
            print("Itens no estoque antes de sair:")
            estoque.mostrar_estoque()  
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("Você deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            print("Itens no estoque antes de sair:")
            estoque.mostrar_estoque()  
            print("Saindo do sistema...")
            break


if __name__ == "__main__":
    main()