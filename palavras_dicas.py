def get_dicas(palavra):    
    dicas = {'banana':'alimento',
    'arroz':'alimento',
    'batata':'alimento',
    'maçã':'alimento',
    'pizza':'alimento',
    'queijo':'alimento',
    'goiaba':'alimento',
    'feijão':'alimento',
    'bife':'alimento',
    'frango':'alimento',
    'sushi':'alimento',
    'jaca':'alimento',
    'açaí':'alimento',
    'alface':'alimento',
    'amora':'alimento',
    'aipim':'alimento',
    'empada':'alimento',
    'paçoca':'alimento',
    'tacos':'alimento',
    'vagem':'alimento',
    'televisor':'eletrodoméstico',
    'monitor':'eletrodoméstico',
    'grill':'eletrodoméstico',
    'freezer':'eletrodoméstico',
    'fritadeira':'eletrodoméstico',
    'sanduicheira':'eletrodoméstico',
    'liquidificador':'eletrodoméstico',
    'bebedouro':'eletrodoméstico',
    'cafeteira':'eletrodoméstico',
    'torradeira':'eletrodoméstico',
    'batedeira':'eletrodoméstico',
    'tanquinho':'eletrodoméstico',
    'refrigerador':'eletrodoméstico',
    'lavadora':'eletrodoméstico',
    'cooktop':'eletrodoméstico',
    'projetor':'eletrodoméstico',
    'aspirador':'eletrodoméstico',
    'secador':'eletrodoméstico',
    'indentação':'programação',
    'algoritmização':'programação',
    'backend':'programação',
    'comitar':'programação',
    'debugger':'programação',
    'framework':'programação',
    'funfar':'programação',
    'fullstack':'programação',
    'refatoração':'programação',
    'overflow':'programação',
    'interpreter':'programação',
    'prompt':'programação',
    'branch':'programação',
    'checkout':'programação',
    'query':'programação',
    'socket':'programação',
    'bootstrap':'programação',
    'jquery':'programação',
    'middleware':'programação',
    'backlog':'programação',
    'suricata':'animal',
    'ariranha':'animal',
    'dioneia':'planta',
    'utricularia':'planta carnívora',
    'sarracenia':'planta carnívora',
    'aquecedor':'eletrodoméstico',
    'ventilador':'eletrodoméstico',
    }
    return dicas.get(palavra, '')