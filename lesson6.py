korona = """
                  .       |         .    .
            .  *         -*-          *
                 \        |         /   .
.    .            .      /^\     .              .    .
   *    |\   /\    /\  / / \ \  /\    /\   /|    *
 .   .  |  \ \/ /\ \ / /     \ \ / /\ \/ /  | .     .
         \ | _ _\/_ _ \_\_ _ /_/_ _\/_ _ \_/
           \  *  *  *   \ \/ /  *  *  *  /
            ` ~ ~ ~ ~ ~  ~\/~ ~ ~ ~ ~ ~ """
chupapupa ="""
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / / / / / / __  / / / / / / / / | | / / / / / / / / /
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \   /..\  ` ` \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
------------------' `---------- (    ) \|/ -----------' `------------------
 ,------------------------- _\___>  <__//` ------------------------------. 
 |/ / / / / / / / / / / / / >,---.   ,-'  / / / / / / / / / / / / / / / /| 
 | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ |  . \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ | 
 |/ / / / / / / / / / / / / / /  `. `. \   ., / / / / / / / / / / / / / /| 
 | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  |  `. | \||_ \ \ \ \ \ \ \ \ \ \ \ \ \ | 
 |/ / / / / / / / / / / / / / / / `.  : |__||   / / / / / / / / / / / / /| 
 | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  __> `.,---'  \ \ \ \ \ \ \ \ \ \ \ \ \ | 
 |/ / / / / / / / / / / / / / /  |.--'\`.\  / / / / / / / / / / / / / / /| 
 `------------------------------ _\\\   \`.| -----------------------------' 
------------------. ,------------ /|\ - |:| ----------. ,------------------
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ ' `    |:|  \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / / / / / / / / / |:| / / / / / | | / / / / / / / / /
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \  |:/  \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / /  --.________,-_/  / / / / / | | / / / / / / / / /
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ ```-----' \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / / / / / / / / / / / / / / / / | | / / / / / / / """

pirog ="""
         (
          )
     __..---..__
 ,-='  /  |  \  `=-.
:--..___________..--;
 \.,_____________,./"""
devil ="""
      |_|   ,
     ('.') ///
     <(_)`-/'
 <-._/J L /  """
zlupapupa ="""
                            ___......__             _
                        _.-'           ~-_       _.=a~~-_
--=====-.-.-_----------~   .--.       _   -.__.-~ ( ___===>
              '''--...__  (    \ \\\ { )       _.-~
                        =_ ~_  \\-~~~//~~~~-=-~
                         |-=-~_ \\   \\
                         |_/   =. )   ~}
                         |}      ||
                        //       ||
                      _//        {{
                   '='~'          \\_    =
                                   ~~'"""
print("ты далеко от дома. нашел красивую корону в пещере, и решил забрать ее. осталось выбраться из пещеры:")
print(korona)
x = input("вправо/влево? --->")
if x != "вправо" and x != "влево":
    c = input("введи нормально:")
    x = c
if x == "вправо":
    print("тебя убил чупапупа(")
    print(chupapupa)
    quit()
elif x == "влево":
    print("тебе повезло, идем дальше!")
print("тебе захотелось кушац, на столе стоит пирог")
print(pirog)
y = input("есть/не есть? --->")
if y != "есть" and y != "не есть":
    d = input("введи нормально:")
    y = d
if y == "есть":
    print("тебя отравили!")
    print(devil)
    quit()
elif y == "не есть":
    print("тебе повезло, идем дальше!")
print("ты встретил монстра. бороться или постараться быть скрытным?")
print(zlupapupa)
z = input("бой/мир? --->")
if z != "бой" and z != "мир":
    o = input("введи нормально:")
    z = o
if z == "бой":
    print("тебе не хватило сил(")
    print(devil)
    quit()
elif x == "мир":
    print("ты выбрался!!!")



    
