import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import re
import os

def generate_fortran_code(question):
    """Gera um código Fortran com base na pergunta."""
    question = question.lower()
    print(f"Pergunta recebida: {question}")  # Depuração

    # Padrões de perguntas e códigos Fortran correspondentes
    if re.search(r'energia cin[ée]tica', question):
        print("Reconhecido: energia cinética")  # Depuração
        return """program kinetic_energy
        implicit none
        real :: m, v, ke
        print *, 'Digite a massa (kg):'
        read *, m
        print *, 'Digite a velocidade (m/s):'
        read *, v
        ke = 0.5 * m * v**2
        print *, 'Energia Cinética:', ke, 'J'
        end program kinetic_energy"""
    elif re.search(r'segunda lei de newton', question):
        print("Reconhecido: segunda lei de newton")  # Depuração
        return """program newton_law
        implicit none
        real :: m, a, f
        print *, 'Digite a massa (kg):'
        read *, m
        print *, 'Digite a aceleracao (m/s^2):'
        read *, a
        f = m * a
        print *, 'Força:', f, 'N'
        end program newton_law"""
    elif re.search(r'n[úu]meros complexos', question):
        print("Reconhecido: números complexos")  # Depuração
        return """program complex_numbers
        implicit none
        complex :: z1, z2, result
        print *, 'Digite o número complexo 1 (a,b):'
        read *, z1
        print *, 'Digite o número complexo 2 (a,b):'
        read *, z2
        result = z1 + z2
        print *, 'Soma dos números complexos:', result
        end program complex_numbers"""
    elif re.search(r'polin[ôo]mios', question):
        print("Reconhecido: polinômios")  # Depuração
        return """program polynomials
        implicit none
        real :: a, b, c, x, result
        print *, 'Digite os coeficientes a, b e c:'
        read *, a, b, c
        print *, 'Digite o valor de x:'
        read *, x
        result = a*x**2 + b*x + c
        print *, 'Valor do polinômio:', result
        end program polynomials"""
    elif re.search(r'logaritmo', question):
        print("Reconhecido: logaritmo")  # Depuração
        return """program logarithm
        implicit none
        real :: x, base, result
        print *, 'Digite o número:'
        read *, x
        print *, 'Digite a base:'
        read *, base
        result = log(x) / log(base)
        print *, 'Logaritmo:', result
        end program logarithm"""
    elif re.search(r'limite', question):
        print("Reconhecido: limite")  # Depuração
        return """program limit_function
        implicit none
        real :: x, h, limit_value
        print *, 'Digite o ponto de aproximação:'
        read *, x
        print *, 'Digite o incremento (h pequeno):'
        read *, h
        limit_value = ((x + h)**2 - x**2) / h  # Corrigido
        print *, 'Aproximação do limite:', limit_value
        end program limit_function"""
    elif re.search(r'área do círculo|área de um círculo', question):
        print("Reconhecido: área do círculo")  # Depuração
        return """program area_circle
        implicit none
        real :: r, area
        real, parameter :: pi = 3.14159
        print *, 'Digite o raio do círculo:'
        read *, r
        area = pi * r**2
        print *, 'Área do círculo:', area
        end program area_circle"""
    elif re.search(r'equação quadrática|raízes de uma equação quadrática', question):
        print("Reconhecido: equação quadrática")  # Depuração
        return """program quadratic_equation
        implicit none
        real :: a, b, c, discriminant, root1, root2
        print *, 'Digite os coeficientes a, b e c:'
        read *, a, b, c
        discriminant = b**2 - 4*a*c
        if (discriminant > 0) then
            root1 = (-b + sqrt(discriminant)) / (2*a)
            root2 = (-b - sqrt(discriminant)) / (2*a)
            print *, 'Raízes reais e distintas:', root1, root2
        else if (discriminant == 0) then
            root1 = -b / (2*a)
            print *, 'Raiz real única:', root1
        else
            print *, 'Raízes complexas.'
        end if
        end program quadratic_equation"""
    elif re.search(r'velocidade média|calcular velocidade média', question):
        print("Reconhecido: velocidade média")  # Depuração
        return """program average_speed
        implicit none
        real :: distance, time, speed
        print *, 'Digite a distância percorrida (metros):'
        read *, distance
        print *, 'Digite o tempo gasto (segundos):'
        read *, time
        speed = distance / time
        print *, 'Velocidade média:', speed, 'm/s'
        end program average_speed"""
    elif re.search(r'volume de uma esfera|calcular volume de uma esfera', question):
        print("Reconhecido: volume de uma esfera")  # Depuração
        return """program volume_esfera
        implicit none
        real :: raio, volume
        real, parameter :: pi = 3.14159
        print *, 'Digite o raio da esfera:'
        read *, raio
        volume = (4.0 / 3.0) * pi * raio**3
        print *, 'Volume da esfera:', volume
        end program volume_esfera"""
    elif re.search(r'celsius para fahrenheit|converter celsius para fahrenheit', question):
        print("Reconhecido: Celsius para Fahrenheit")  # Depuração
        return """program celsius_to_fahrenheit
        implicit none
        real :: celsius, fahrenheit
        print *, 'Digite a temperatura em Celsius:'
        read *, celsius
        fahrenheit = (celsius * 9.0 / 5.0) + 32.0
        print *, 'Temperatura em Fahrenheit:', fahrenheit
        end program celsius_to_fahrenheit"""
    elif re.search(r'fatorial|calcular fatorial', question):
        print("Reconhecido: fatorial")  # Depuração
        return """program fatorial
        implicit none
        integer :: n, i, fatorial
        print *, 'Digite um número inteiro:'
        read *, n
        fatorial = 1
        do i = 1, n
            fatorial = fatorial * i
        end do
        print *, 'Fatorial de ', n, ' é ', fatorial
        end program fatorial"""
    elif re.search(r'hipotenusa|calcular hipotenusa', question):
        print("Reconhecido: hipotenusa")  # Depuração
        return """program hipotenusa
        implicit none
        real :: a, b, hipotenusa
        print *, 'Digite o valor do cateto a:'
        read *, a
        print *, 'Digite o valor do cateto b:'
        read *, b
        hipotenusa = sqrt(a**2 + b**2)
        print *, 'Hipotenusa:', hipotenusa
        end program hipotenusa"""
    elif re.search(r'média aritmética|calcular média aritmética', question):
        print("Reconhecido: média aritmética")  # Depuração
        return """program media_aritmetica
        implicit none
        real :: a, b, c, media
        print *, 'Digite três números:'
        read *, a, b, c
        media = (a + b + c) / 3.0
        print *, 'Média aritmética:', media
        end program media_aritmetica"""
    elif re.search(r'perímetro de um círculo|calcular perímetro de um círculo', question):
        print("Reconhecido: perímetro de um círculo")  # Depuração
        return """program perimetro_circulo
        implicit none
        real :: raio, perimetro
        real, parameter :: pi = 3.14159
        print *, 'Digite o raio do círculo:'
        read *, raio
        perimetro = 2.0 * pi * raio
        print *, 'Perímetro do círculo:', perimetro
        end program perimetro_circulo"""
    elif re.search(r'área de um triângulo|calcular área de um triângulo', question):
        print("Reconhecido: área de um triângulo")  # Depuração
        return """program area_triangulo
        implicit none
        real :: base, altura, area
        print *, 'Digite a base do triângulo:'
        read *, base
        print *, 'Digite a altura do triângulo:'
        read *, altura
        area = (base * altura) / 2.0
        print *, 'Área do triângulo:', area
        end program area_triangulo"""
    elif re.search(r'juros simples|calcular juros simples', question):
        print("Reconhecido: juros simples")  # Depuração
        return """program juros_simples
        implicit none
        real :: principal, taxa, tempo, juros
        print *, 'Digite o valor principal:'
        read *, principal
        print *, 'Digite a taxa de juros (em decimal):'
        read *, taxa
        print *, 'Digite o tempo (em anos):'
        read *, tempo
        juros = principal * taxa * tempo
        print *, 'Juros simples:', juros
        end program juros_simples"""
    elif re.search(r'distância entre dois pontos|calcular distância entre dois pontos', question):
        print("Reconhecido: distância entre dois pontos")  # Depuração
        return """program distancia_pontos
        implicit none
        real :: x1, y1, x2, y2, distancia
        print *, 'Digite as coordenadas do primeiro ponto (x1, y1):'
        read *, x1, y1
        print *, 'Digite as coordenadas do segundo ponto (x2, y2):'
        read *, x2, y2
        distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print *, 'Distância entre os pontos:', distancia
        end program distancia_pontos"""
    elif re.search(r'volume de um cilindro|calcular volume de um cilindro', question):
        print("Reconhecido: volume de um cilindro")  # Depuração
        return """program volume_cilindro
        implicit none
        real :: raio, altura, volume
        real, parameter :: pi = 3.14159
        print *, 'Digite o raio da base do cilindro:'
        read *, raio
        print *, 'Digite a altura do cilindro:'
        read *, altura
        volume = pi * raio**2 * altura
        print *, 'Volume do cilindro:', volume
        end program volume_cilindro"""
    elif re.search(r'volume de um cubo|calcular volume de um cubo', question):
        print("Reconhecido: volume de um cubo")  # Depuração
        return """program volume_cubo
        implicit none
        real :: lado, volume
        print *, 'Digite o lado do cubo:'
        read *, lado
        volume = lado**3
        print *, 'Volume do cubo:', volume
        end program volume_cubo"""
    elif re.search(r'fahrenheit para celsius|converter fahrenheit para celsius', question):
        print("Reconhecido: Fahrenheit para Celsius")  # Depuração
        return """program fahrenheit_to_celsius
        implicit none
        real :: fahrenheit, celsius
        print *, 'Digite a temperatura em Fahrenheit:'
        read *, fahrenheit
        celsius = (fahrenheit - 32.0) * 5.0 / 9.0
        print *, 'Temperatura em Celsius:', celsius
        end program fahrenheit_to_celsius"""
    elif re.search(r'perímetro de um retângulo|calcular perímetro de um retângulo', question):
        print("Reconhecido: perímetro de um retângulo")  # Depuração
        return """program perimetro_retangulo
        implicit none
        real :: comprimento, largura, perimetro
        print *, 'Digite o comprimento do retângulo:'
        read *, comprimento
        print *, 'Digite a largura do retângulo:'
        read *, largura
        perimetro = 2.0 * (comprimento + largura)
        print *, 'Perímetro do retângulo:', perimetro
        end program perimetro_retangulo"""
    elif re.search(r'área de um retângulo|calcular área de um retângulo', question):
        print("Reconhecido: área de um retângulo")  # Depuração
        return """program area_retangulo
        implicit none
        real :: comprimento, largura, area
        print *, 'Digite o comprimento do retângulo:'
        read *, comprimento
        print *, 'Digite a largura do retângulo:'
        read *, largura
        area = comprimento * largura
        print *, 'Área do retângulo:', area
        end program area_retangulo"""
    elif re.search(r'volume de um paralelepípedo|calcular volume de um paralelepípedo', question):
        print("Reconhecido: volume de um paralelepípedo")  # Depuração
        return """program volume_paralelepipedo
        implicit none
        real :: comprimento, largura, altura, volume
        print *, 'Digite o comprimento do paralelepípedo:'
        read *, comprimento
        print *, 'Digite a largura do paralelepípedo:'
        read *, largura
        print *, 'Digite a altura do paralelepípedo:'
        read *, altura
        volume = comprimento * largura * altura
        print *, 'Volume do paralelepípedo:', volume
        end program volume_paralelepipedo"""
    elif re.search(r'área de um trapézio|calcular área de um trapézio', question):
        print("Reconhecido: área de um trapézio")  # Depuração
        return """program area_trapezio
        implicit none
        real :: base_maior, base_menor, altura, area
        print *, 'Digite a base maior do trapézio:'
        read *, base_maior
        print *, 'Digite a base menor do trapézio:'
        read *, base_menor
        print *, 'Digite a altura do trapézio:'
        read *, altura
        area = ((base_maior + base_menor) * altura) / 2.0
        print *, 'Área do trapézio:', area
        end program area_trapezio"""
    elif re.search(r'volume de uma pirâmide|calcular volume de uma pirâmide', question):
        print("Reconhecido: volume de uma pirâmide")  # Depuração
        return """program volume_piramide
        implicit none
        real :: area_base, altura, volume
        print *, 'Digite a área da base da pirâmide:'
        read *, area_base
        print *, 'Digite a altura da pirâmide:'
        read *, altura
        volume = (area_base * altura) / 3.0
        print *, 'Volume da pirâmide:', volume
        end program volume_piramide"""
    elif re.search(r'área de um losango|calcular área de um losango', question):
        print("Reconhecido: área de um losango")  # Depuração
        return """program area_losango
        implicit none
        real :: diagonal_maior, diagonal_menor, area
        print *, 'Digite a diagonal maior do losango:'
        read *, diagonal_maior
        print *, 'Digite a diagonal menor do losango:'
        read *, diagonal_menor
        area = (diagonal_maior * diagonal_menor) / 2.0
        print *, 'Área do losango:', area
        end program area_losango"""
    elif re.search(r'volume de um cone|calcular volume de um cone', question):
        print("Reconhecido: volume de um cone")  # Depuração
        return """program volume_cone
        implicit none
        real :: raio, altura, volume
        real, parameter :: pi = 3.14159
        print *, 'Digite o raio da base do cone:'
        read *, raio
        print *, 'Digite a altura do cone:'
        read *, altura
        volume = (pi * raio**2 * altura) / 3.0
        print *, 'Volume do cone:', volume
        end program volume_cone"""
    elif re.search(r'área de um setor circular|calcular área de um setor circular', question):
        print("Reconhecido: área de um setor circular")  # Depuração
        return """program area_setor_circular
        implicit none
        real :: raio, angulo, area
        real, parameter :: pi = 3.14159
        print *, 'Digite o raio do círculo:'
        read *, raio
        print *, 'Digite o ângulo do setor circular (em graus):'
        read *, angulo
        area = (pi * raio**2 * angulo) / 360.0
        print *, 'Área do setor circular:', area
        end program area_setor_circular"""
    else:
        print("Pergunta não reconhecida.")  # Depuração
        return None

def execute_fortran_code(code):
    """Executa um código Fortran e retorna o output."""
    file_path = "calculo.f90"
    with open(file_path, "w") as f:
        f.write(code)
    
    try:
        # Compila o código Fortran
        compile_result = subprocess.run(
            ["gfortran", file_path, "-o", "calculo"],
            capture_output=True,
            text=True
        )
        if compile_result.returncode != 0:
            return f"Erro de compilação:\n{compile_result.stderr}"
        
        # Executa o binário gerado
        run_result = subprocess.run(
            ["./calculo"],
            input="5\n3\n",  # Entrada como string
            text=True,
            capture_output=True
        )
        if run_result.returncode != 0:
            return f"Erro de execução:\n{run_result.stderr}"
        
        return run_result.stdout
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def calculate():
    """Obtém a pergunta do usuário, gera e executa o código Fortran."""
    question = entry.get()
    print(f"Pergunta obtida: {question}")  # Depuração
    fortran_code = generate_fortran_code(question)
    
    if fortran_code:
        # Limpa a caixa de texto
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        
        # Exibe o código Fortran gerado
        result_text.insert(tk.END, "Código Fortran Gerado:\n")
        result_text.insert(tk.END, "-" * 50 + "\n")
        result_text.insert(tk.END, fortran_code + "\n")
        result_text.insert(tk.END, "-" * 50 + "\n\n")
        
        # Executa o código Fortran e exibe o resultado
        output = execute_fortran_code(fortran_code)
        result_text.insert(tk.END, "Resultado da Execução:\n")
        result_text.insert(tk.END, "-" * 50 + "\n")
        result_text.insert(tk.END, output + "\n")
        
        # Desabilita a edição da caixa de texto
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Erro", "Pergunta não reconhecida. Tente outra fórmula matemática ou física.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Calculadora Avançada de Física, Engenharia e Matemática")
root.geometry("600x500")

tk.Label(root, text="Digite sua pergunta:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Calcular", font=("Arial", 12), command=calculate).pack(pady=5)

result_text = scrolledtext.ScrolledText(root, width=70, height=15, font=("Arial", 10), state=tk.DISABLED)
result_text.pack(pady=10)

root.mainloop()