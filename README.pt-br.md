<h1 width="100%">
  <img src="img/Logo.png" align="center"/>
</h1>
<div class="badges" align="center">
  <img src="https://img.shields.io/static/v1?label=Linguagem&labelColor=D18CE0&message=Python&color=F6F5F2&style=for-the-badge&logo=visualstudiocode"/>
  <img src="https://img.shields.io/static/v1?label=Situacao&labelColor=D18CE0&message=Finalizado&color=F6F5F2&style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/static/v1?label=Versao&labelColor=D18CE0&message=1.1.0&color=F6F5F2&style=for-the-badge&logo=vonage"/>
  <img src="https://img.shields.io/static/v1?label=Licenca&labelColor=D18CE0&message=MIT&color=F6F5F2&style=for-the-badge&logo=perforce"/>
</div>
<br>
<h2 id="about">1. Sobre</h2>
<p>
  Este software foi projetado para coletar dados da calculadora do Google AdSense usando o Selenium para automação web. Ele usa o customtkinter para a interface gráfica do usuário (GUI), OpenCV e Tesseract para processamento de imagem e reconhecimento óptico de caracteres (OCR), e Matplotlib e pandas para análise e visualização de dados.
</p>
<br/>

<h2 id="summary">2. Sumário</h2>
<details open>
  <summary>Sumário</summary><br>
  A aplicação automatiza o processo de seleção de categorias e regiões do calculador do Google AdSense, captura os resultados exibidos usando capturas de tela, extrai texto das imagens usando OCR e armazena os dados em um arquivo CSV. Em seguida, gera gráficos visuais para uma análise mais aprofundada dos dados coletados.<br/>
  
  * [Sobre](#about)
    
  * [Sumário](#summary)
    <details open>
    <summary target="#howtouse">Como usar</summary>

    * [Pré-requisitos](#prerequisites)
    * [Instalação do Tesseract](#tesseract_instalation)
    * [Tutorial da Interface](#interface_tutorial)
    * [Interpretação de Dados](#data_interpretation)
      <details closed>
      <summary target="#extra">Extra</summary>
      
        * [Integração com Excel](#excel_integration)
      </details>
    </details>
    
    <details open>
      <summary target="#howitworks">Como funciona?</summary>

    * [Interação com a Interface](#interface_interaction)
    
    * [Processo de Automação](#automation_process)
      
    * [Captura de Imagem](#image_capture)
      
    * [Extração de Texto](#text_extraction)
      
    * [Armazenamento de Dados](#data_storage)
   
    * [Coleta de Dados](#data_collection)
      
    * [Criação de Gráficos](#chart_creation)
    </details>

  * [Testes](#tests)
    
  * [Tecnologias](#technologies)
</details>

<br>
<h2 id="howtouse">3. Como usar</h2>
  <h3 id="prerequisites">3.1 Pré-requisitos</h3>
  <ul>
        <li>Python 3.x</li>
        <li>Selenium</li>
        <li>OpenCV</li>
        <li>Pytesseract</li>
        <li>Matplotlib</li>
        <li>Pandas</li>
        <li>CustomTkinter</li>
    </ul><br>
  <h3 id="tesseract_instalation">3.2 Instalação do Tesseract</h3>
  <ol>
        <li>Faça o download do instalador do Tesseract em <a href="https://github.com/tesseract-ocr/tesseract">Tesseract GitHub</a>.</li>
        <li>Execute o instalador e siga as instruções.</li>
        <li>Adicione o caminho de instalação do Tesseract à variável de ambiente PATH do seu sistema.</li>
    </ol><br>
  <h3 id="interface_tutorial">3.3 Tutorial da Interface</h3>
    <p>Esta seção fornece um guia detalhado sobre como navegar e usar a interface gráfica do usuário (GUI) do software para coletar dados do calculador do Google AdSense.</p>
    <h4>Guia Passo a Passo para Usar a Interface</h4>
    <h5>1. Iniciando a Interface</h5>
    <p>
        Certifique-se de que todas as dependências estejam instaladas e configuradas corretamente, incluindo o Tesseract e o driver da web.<br>
        Execute o script <code>interface.py</code> usando Python:
    </p>
    <pre><code>python interface.py</code></pre>
    <p>
        Isso abrirá a janela principal da GUI intitulada "Google AdSense - Data Collector".
    </p>
    <h5>2. Entendendo o Layout da Janela Principal</h5>
    <p>
        A janela está dividida em dois frames roláveis:
    </p>
    <ul>
        <li><strong>Frame Esquerdo (Regiões)</strong>: Contém caixas de seleção para escolher as regiões.</li>
        <li><strong>Frame Direito (Categorias)</strong>: Contém caixas de seleção para escolher as categorias.</li>
    </ul>
    <h5>3. Selecionando Regiões</h5>
    <p>
        As regiões são exibidas no frame rolável esquerdo.<br>
        As regiões disponíveis são:
    </p>
    <ul>
        <li>América do Norte</li>
        <li>América do Sul</li>
        <li>Europa, Oriente Médio e África</li>
        <li>Ásia e países do Pacífico</li>
    </ul>
    <p>
        Clique na caixa de seleção ao lado de cada região que deseja incluir na coleta de dados.
    </p>
    <h5>4. Selecionando Categorias</h5>
    <p>
        As categorias são exibidas no frame rolável direito.<br>
        As categorias disponíveis incluem:
    </p>
    <ul>
        <li>Artes e entretenimento</li>
        <li>Automóveis e veículos</li>
        <li>Casa e jardim</li>
        <li>Ciência</li>
        <li>Comida e bebidas</li>
        <li>Compras</li>
        <li>E muitas outras (conforme listado no script inicial)</li>
    </ul>
    <p>
        Você pode selecionar individualmente as categorias clicando nas caixas de seleção ao lado de cada uma.
    </p>
    <h5>5. Usando a Função "Selecionar Tudo"</h5>
    <p>
        No topo do frame rolável direito, há uma caixa de seleção "Selecionar Tudo".<br>
        Clicar nesta caixa de seleção selecionará ou desmarcará todas as caixas de seleção das categorias:
    </p>
    <ul>
        <li>Se desejar selecionar todas as categorias, marque esta caixa.</li>
        <li>Se desejar desmarcar todas as categorias, desmarque esta caixa.</li>
    </ul>
    <h5>6. Confirmar Seleções</h5>
    <p>
        Após selecionar as regiões e categorias desejadas, clique no botão "Confirmar" na parte inferior central da janela.<br>
        O botão de confirmação inicia o processo de coleta de dados:
    </p>
    <ul>
        <li>Se alguma região ou categoria não estiver selecionada, será exibida uma mensagem indicando que há opções não selecionadas.</li>
        <li>Garanta que pelo menos uma região e uma categoria estejam selecionadas antes de clicar em "Confirmar".</li>
    </ul><br>
  <h3 id="data_collection">3.4 Coleta de Dados</h3><br/>
  <p>O processo de coleta de informações envolve várias etapas:</p>
    <ol>
        <li><strong>Inicialização:</strong> O software inicializa o Selenium e abre o site do Google AdSense. As credenciais de login fornecidas pelo usuário são usadas para autenticar e acessar as páginas de dados necessárias.</li>
        <li><strong>Navegação:</strong> O Selenium automatiza a navegação pelo site do Google AdSense. Ele seleciona as regiões e categorias especificadas com base na entrada do usuário.</li>
        <li><strong>Captura de Captura de Tela:</strong> Uma vez que os dados relevantes são exibidos, o software captura capturas de tela das páginas da web usando a biblioteca pyscreenshot.</li>
        <li><strong>Processamento de Imagem:</strong> As capturas de tela capturadas são processadas usando o OpenCV para melhorar a qualidade das imagens. Isso inclui redução de ruído, limiarização e detecção de bordas para preparar as imagens para o OCR.</li>
        <li><strong>Extração de Texto:</strong> O Pytesseract é usado para extrair texto das imagens processadas. O texto extraído é analisado para identificar os valores numéricos necessários e as categorias associadas.</li>
        <li><strong>Armazenamento de Dados:</strong> Os dados extraídos são organizados e salvos em um arquivo CSV localizado em <code>data/info.csv</code>. Este arquivo contém colunas para a categoria, valor, região e status (indicando se os dados foram coletados na primeira tentativa ou revisados).</li>
    </ol><br>
  <h3 id="data_interpretation">3.5 Interpretação de Dados</h3><br/>
  <p>Após a coleta de dados, eles são salvos em um arquivo CSV localizado em <code>data/info.csv</code>. Os dados incluem as seguintes colunas:</p>
    <ul>
        <li><strong>Categoria:</strong> A categoria do anúncio.</li>
        <li><strong>Valor:</strong> O valor coletado para a categoria.</li>
        <li><strong>Região:</strong> A região associada aos dados.</li>
        <li><strong>Status:</strong> Indica se os dados foram coletados na primeira tentativa ou revisados.</li>
    </ul><br>
  <h3 id="extra">3.6 Extra</h3>
    <h3 id="excel_integration">Integração com Excel</h4>
    <ol>
      <li>
        <h4>Abrir o Excel e Importar os Dados do CSV:</h4>
        <ul>
          <li>Abra o Excel e crie uma nova planilha.</li>
          <li>Vá para a guia "Dados" e clique em "De Texto/CSV".</li>
          <li>Selecione o arquivo CSV gerado pelo seu programa que contém os dados que você deseja usar para o gráfico e clique em "Importar".</li>
        </ul>
      </li>
      <li>
        <h4>Configurar a Importação:</h4>
        <ul>
          <li>Na janela de importação, certifique-se de que o delimitador e o tipo de dados estão corretos. O Excel geralmente detecta automaticamente o delimitador e o tipo de dados.</li>
          <li>Clique em "Carregar" para importar os dados para o Excel.</li>
        </ul>
      </li>
      <li>
        <h4>Criar uma Tabela Dinâmica:</h4>
        <ul>
          <li>Com os dados importados na planilha, selecione qualquer célula dentro da faixa de dados.</li>
          <li>Vá para a guia "Inserir" e clique em "Tabela Dinâmica". Escolha "Tabela Dinâmica" no menu suspenso.</li>
          <li>Na janela "Criar Tabela Dinâmica", confirme que a faixa de dados está correta e escolha onde deseja colocar a Tabela Dinâmica na planilha. Clique em "OK".</li>
        </ul>
      </li>
      <li>
        <h4>Configurar a Tabela Dinâmica:</h4>
        <ul>
          <li>Na nova área à direita, você verá campos como "Rótulos de Linha", "Rótulos de Coluna", "Valores", etc.</li>
          <li>Arraste os campos relevantes para as áreas desejadas. Por exemplo, você pode colocar o campo "Category" em "Rótulos de Linha" e o campo "Values" em "Valores".</
                    <li>Isso criará uma Tabela Dinâmica resumindo os dados com base na sua configuração.</li>
        </ul>
      </li>
      <li>
        <h4>Criar o Gráfico da Tabela Dinâmica:</h4>
        <ul>
          <li>Com a Tabela Dinâmica configurada, selecione qualquer célula dentro dela.</li>
          <li>Vá para a guia "Inserir" e clique em "Gráfico de Tabela Dinâmica". Escolha o tipo de gráfico que deseja criar (por exemplo, gráfico de colunas, gráfico de linhas, gráfico de pizza, etc.).</li>
          <li>Depois de criar o gráfico, você pode ajustar detalhes como títulos, legendas, cores etc., clicando com o botão direito no gráfico e selecionando as opções desejadas.</li>
        </ul>
      </li>
      <li>
        <h4>Atualizar o Gráfico da Tabela Dinâmica:</h4>
        <ul>
          <li>Sempre que seus dados no CSV forem atualizados ou novos dados forem adicionados, você pode atualizar o gráfico da Tabela Dinâmica clicando com o botão direito na Tabela Dinâmica e selecionando "Atualizar".</li>
        </ul>
      </li>
    </ol>
<br>
<h2 id="howitworks">4. Como funciona?</h2>
  <h3 id="interface_interaction">4.1 Interação com a Interface</h3>
    <p>A interface é construída usando CustomTkinter, fornecendo uma GUI simples para selecionar regiões e categorias para a coleta de dados.</p>
    <h3 id="automation_process">4.2 Processo de Automação</h3>
    <p>O processo de automação usa o Selenium para navegar no site do Google AdSense, selecionando regiões e categorias com base na entrada do usuário.</p>
    <h3 id="image_capture">4.3 Captura de Imagem</h3>
    <p>O software captura capturas de tela dos resultados exibidos no site usando a biblioteca pyscreenshot.</p>
    <h3 id="text_extraction">4.4 Extração de Texto</h3>
    <p>Texto extraído das capturas de tela usando OCR do Tesseract é processado para remover caracteres não numéricos e obter os valores desejados.</p>
    <h3 id="data_storage">4.5 Armazenamento de Dados</h3>
    <p>Os dados coletados são armazenados em um arquivo CSV para análise e visualização posterior.</p>
    <h3 id="chart_creation">4.6 Criação de Gráficos</h3>
    <p>Os dados armazenados são usados para criar gráficos visuais usando Matplotlib, fornecendo uma representação gráfica dos valores de anúncios em diferentes regiões e categorias.</p><br>

<h2 id="tests">5. Testes</h2>
<p>Para garantir que o software funcione corretamente, os seguintes testes podem ser executados para verificar:</p>
    <ul>
        <li>Instalação correta das dependências.</li>
        <li>Funcionalidade correta da automação web do Selenium.</li>
        <li>Precisão da extração de texto OCR do Tesseract.</li>
        <li>Integridade dos dados no arquivo CSV.</li>
        <li>Geração correta de gráficos visuais.</li>
    </ul>
<br>
<h2 id="technologies">6. Tecnologias</h2>
<p>Este projeto utiliza as seguintes tecnologias:</p>
    <ul>
        <li><strong>Python:</strong> A linguagem de programação principal usada para o desenvolvimento.</li>
        <li><strong>Selenium:</strong> Usado para automação web e interação.</li>
        <li><strong>OpenCV:</strong> Usado para tarefas de processamento de imagem.</li>
        <li><strong>Pytesseract:</strong> Utilizado para Reconhecimento Óptico de Caracteres (OCR).</li>
        <li><strong>pyscreenshot:</strong> Usado para captura de capturas de tela.</li>
        <li><strong>CustomTkinter:</strong> Usado para criar a interface gráfica do usuário.</li>
        <li><strong>Pandas:</strong> Usado para manipulação e análise de dados.</li>
        <li><strong>Matplotlib:</strong> Usado para criar gráficos visuais.</li>
    </ul>

