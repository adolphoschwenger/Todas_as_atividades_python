import time

# Função para o cronômetro
def cronometro():
    print("Pressione Enter para iniciar o cronômetro.")
    print("Pressione Ctrl+C para parar o cronômetro.")
    
    try:
        input()  # Espera o usuário pressionar Enter para iniciar
        start_time = time.time()
        print("Cronômetro iniciado!")
        
        while True:
            elapsed_time = time.time() - start_time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            print(f"\rTempo decorrido: {formatted_time}", end="")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nCronômetro parado.")
        elapsed_time = time.time() - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print(f"Tempo total: {formatted_time}")

# Executa o cronômetro
if __name__ == "__main__":
    cronometro()