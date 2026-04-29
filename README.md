# festival

## Alteracoes feitas

Neste trabalho completei varias funcionalidades que estavam em falta ou que
estavam apenas parcialmente implementadas na aplicacao Django.

Primeiro analisei os ficheiros principais da app, principalmente `models.py`,
`forms.py`, `views.py`, `urls.py` e os templates. A partir disso percebi que ja
existiam os modelos para bandas, dias, palcos e concertos, mas algumas paginas
nao estavam totalmente ligadas entre si.

Na listagem dos dias, alterei a view para os dias aparecerem ordenados por data
crescente. Para isso usei `Dia.objects.order_by("data")` em `dias_view`, no
ficheiro `festival/views.py`.

Tambem corrigi o formulario de edicao de concertos. Antes so era possivel editar
a hora do concerto. Agora o formulario permite editar a banda, o palco, o dia e
a hora, atraves do `ConcertoForm` em `festival/forms.py`.

Implementei a criacao de concertos. O link "Criar concerto" no menu agora abre
uma pagina com um formulario, onde se pode escolher uma banda existente, o palco,
o dia e a hora. Para isto criei a view, a rota e o template
`festival/templates/festival/criar_concerto.html`.

Tambem implementei a eliminacao de concertos. Na pagina de detalhe de um
concerto existe agora um botao para apagar. Esse botao esta dentro de um
formulario com `method="post"` e usa `csrf_token`, para garantir que a eliminacao
so acontece atraves de POST.

No modelo `Palco`, adicionei o campo booleano
`acessibilidade_mobilidade_reduzida`, com valor padrao `False`. Depois criei e
apliquei a migracao correspondente. A listagem dos palcos foi atualizada para
mostrar o nome, a capacidade, o numero total de concertos agendados e o simbolo
de acessibilidade quando esse campo esta ativo.

Por fim, implementei a edicao de palcos. O botao "Editar palco" agora funciona e
abre um formulario onde se pode alterar o nome, a capacidade e a acessibilidade
para mobilidade reduzida.

## Ordenacao dos concertos

No modelo `Concerto`, a linha:

```python
ordering = ["dia__data", "hora"]
```

define a ordenacao padrao dos concertos. O campo `dia__data` usa a relacao
entre `Concerto` e `Dia` para ordenar primeiro pela data do dia associado ao
concerto. Depois, `hora` ordena os concertos desse mesmo dia pela hora de
inicio.

Assim, sempre que os concertos forem obtidos sem outra ordenacao explicita,
aparecem por ordem cronologica: primeiro o dia mais antigo e, dentro desse dia,
os concertos mais cedo.

Se esta linha fosse removida, o Django deixaria de garantir esta ordem padrao e
os concertos poderiam aparecer numa ordem dependente da base de dados, por
exemplo por id de criacao. Se fosse alterada, a listagem passaria a seguir a
nova regra definida, como ordenar apenas pela hora ou pela banda, o que poderia
misturar concertos de dias diferentes.
