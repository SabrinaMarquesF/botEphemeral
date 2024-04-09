import discord
from discord import app_commands
import random

id_do_servidor =  740729747478282251

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) 
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'sobre', description='Informações sobre o bot')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá, me chamo Ephemeral, sou um viajante e resolvi passar um tempo neste planeta. Que tal conversarmos um pouco? Me chame usando '/'", ephemeral = False)
  
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'criadora', description='Nome da criadora')
async def slash3(interaction: discord.Interaction):
      await interaction.response.send_message(f"Fui desenvolvido por @sxbrinamf https://sxbrinamf.netlify.app", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dadod6', description='Rodar um dado D6')
async def slash4(interaction: discord.Interaction):
      numero = random.randint(1,6)
      await interaction.response.send_message(f"Número {numero}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dadod20', description='Rodar um dado D20')
async def slash5(interaction: discord.Interaction):
      numero = random.randint(1,20)
      await interaction.response.send_message(f"Número {numero}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dadod100', description='Rodar um dado D100')
async def slash6(interaction: discord.Interaction):
      numero = random.randint(1,100)
      await interaction.response.send_message(f"Número {numero}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'comovai', description='Estado de espírito')
async def slash7(interaction: discord.Interaction):
      palavras = ["Vou bem, obrigado!", "Não vou bem, mas obrigado!", "Não quero responder."]
      palavra_aleatoria = random.choice(palavras)
      await interaction.response.send_message(f"{palavra_aleatoria}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'piada', description='Conte uma piada')
async def slash8(interaction: discord.Interaction):
      palavras = ["Por que o peixe não gosta de dividir sua comida? Porque ele é um pouco egoísta.", "Qual é o doce favorito dos astronautas? Mars-mallow!", "Por que o computador foi à escola? Para aprender o sistema binário.", "Por que a galinha atravessou a rua? Para mostrar que ela não é um frango amarelo.", "Como se chama um homem com uma espada na cabeça? Ed-head.", "Por que o livro de matemática parecia triste? Porque tinha muitos problemas.", "Por que o pão não pode ser detetive? Porque ele sempre fica amassado no caso."]
      piada_aleatoria = random.choice(palavras)
      await interaction.response.send_message(f"{piada_aleatoria}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'classe', description='Classe do jogo')
async def slash9(interaction: discord.Interaction):
      palavras = ["Guerreiro", "Mago", "Ladrão (ou Rogue)", "Clérigo", "Bárbado","Druida","Feiticeiro","Bardo","Paladino","Monge","Bruxo","Cavaleiro","Necromante"]
      classe_aleatoria = random.choice(palavras)
      await interaction.response.send_message(f"{classe_aleatoria}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'opina', description='Opine sobre alguém')
async def slash10(interaction: discord.Interaction):
      palavras = ["Você me parece legal!", "Hm, piranha.", "Você é simpático.", "Gentil", "Irritante", "Adoro falar com você <3","Na minha terra lhe chamariam de incel","Um pouco gado","Prefiro não opinar"]
      opina_aleatoria = random.choice(palavras)
      await interaction.response.send_message(f"{opina_aleatoria}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'sobreoserver', description='Sobre o servidor')
async def slash12(interaction: discord.Interaction):
      await interaction.response.send_message(f"O servidor foi criado dia 05 de ago. de 2020 com o intuito de reunir pessoas com gostos em comum por games e RPG. Leia as regras e convide seus amigos  https://discord.gg/qnag5nKgqg", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dadod8', description='Rodar um dado D8')
async def slash13(interaction: discord.Interaction):
      numero = random.randint(1,8)
      await interaction.response.send_message(f"Número {numero}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'help', description='Lista de comandos')
async def slash14(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá, me chamo Ephemeral, usando '/' posso rolar dados como D6, D8, D20, D100, escolher a classe do seu personagem, opinar sobre você, contar uma piada, te contar curiosidades, falar sobre o servidor, e se você gostar de mim posso dizer como estou :) Veja meus comandos em /comandos", ephemeral = True)


@tree.command(guild = discord.Object(id=id_do_servidor), name = 'curiosidade', description='Conto uma curiosidade')
async def slash15(interaction: discord.Interaction):
        palavras = ["Cérebros de Albert Einstein: Após a morte de Albert Einstein em 1955, seu cérebro foi removido durante a autópsia sem permissão da família. Partes do seu cérebro foram preservadas para estudo, e pesquisadores descobriram diferenças sutis em algumas áreas do cérebro de Einstein em comparação com cérebros 'normais'.", "Fungos bioluminescentes: Existem espécies de fungos que emitem luz, conhecidos como fungos bioluminescentes. Eles são frequentemente encontrados em florestas tropicais e podem criar um efeito mágico de luzes brilhantes no ambiente noturno.", "Onda gravitacional: Em 2015, cientistas detectaram ondas gravitacionais pela primeira vez, confirmando uma das previsões fundamentais da teoria da relatividade geral de Einstein. Essas ondas são distorções no espaço-tempo causadas por eventos cósmicos extremamente violentos, como colisões de buracos negros.", "Ossos das aves: As aves têm ossos ocos que as tornam mais leves para voar. Em alguns casos, esses ossos têm estruturas complexas de suporte interno, como asas de avião, para aumentar a resistência e a eficiência do voo.", "Efeito placebo em animais: Alguns estudos sugerem que animais, como cães e cavalos, também podem experimentar o efeito placebo, onde melhoram ou respondem a um tratamento não ativo simplesmente por acreditarem que estão recebendo um medicamento.","Fotossíntese em lagartixas: Algumas espécies de lagartixas têm a capacidade de realizar fotossíntese parcial, onde absorvem a luz solar diretamente através da pele e a utilizam para gerar energia.", "Fusão nuclear nas estrelas: As estrelas geram energia através da fusão nuclear, onde átomos de hidrogênio se combinam para formar hélio. Esse processo libera enormes quantidades de energia e é responsável pela luz e calor emitidos pelas estrelas.", "Memória de elefantes: Os elefantes têm uma memória excepcionalmente boa e podem lembrar de locais de água, rotas de migração e até mesmo indivíduos por muitos anos.", "Picos de montanhas: Os picos das montanhas são afetados pela gravidade mais fraca, o que significa que objetos pesam um pouco menos no topo de uma montanha do que ao nível do mar. Isso também faz com que o ar seja mais rarefeito em altitudes elevadas.", "Nuvens lenticulares: Algumas nuvens têm formas incomuns, como as nuvens lenticulares, que se assemelham a discos ou lentes. Elas são formadas pela interação de ventos e terreno montanhoso e são frequentemente avistadas perto de montanhas altas."]
        curiosidade_aleatoria = random.choice(palavras)
        await interaction.response.send_message(f"{curiosidade_aleatoria}", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'comandos', description='Comandos do Ephemeral')
async def slash16(interaction: discord.Interaction):
    await interaction.response.send_message(f"/sobre: Informações sobre o bot, /criadora: Saiba quem me criou!, /dadod6-d100: rodo o dado que você escolheu, /comovai: falo como estou me sentindo, /piada: conto uma piada para você sorrir, /classe: escolho a classe do seu personagem, /opina: falo o que acho sobre você, /sobreoserver: informações do servidor, /help: explico o que faço, /conto uma curiosidade.", ephemeral = False)


aclient.run('token')
