# Flask-Python-Arduino
Projeto simples que mostra uma aplicação web feita com Flask e Python que controla uma placa Arduino no servidor local

### Flask
Na estrutura do projeto o framework Flask foi usado para gerenciar a rota e os métodos "get" ou "post" que são necessários para a relação entre o front-end e back-end

### Python 
Python foi utilizado para criar a aplicação junto com o Flask e, além disso, para controlar o arduino por meio das bibliotecas importadas

### Arduino
O Arduino utilizado foi o Arduino Uno e foi colocado três leds em suas portas digitais que são controlados pelos botões da página principal

### Componentes utilizados
- 1x placa Arduino Uno
- 3x resistores 220 ohms
- 3x leds (Verde, Vermelho e Amarelo)
- 7x jumpers
- 1x protoboard

### Funcionamento
Para que o projeto funcione é necessário estar com a placa Arduino e o circuito conectados ao computador e identificar qual porta ele está conectado. Além disso a aplicação deverá ser hospedada no servidor local utilizando o comando "flask run". Há botôes de ligar e desligar para cada led, que ao ser clicado liga ou desliga o determinado led instantaneamente
