from datetime import datetime
import random


def random_string(length: int = 5):
    sample_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(sample_characters) for x in range(length))


def random_number(length: int = 3):
    sample_numbers = "0123456789"
    return ''.join(random.choice(sample_numbers) for x in range(length))


def random_email():
    return random_string(5) + "." + random_string(5) + random_number(3) + "@gmail.com"


def get_date_offset_years(offset_years: int = -20, date_format="%d-%m-%Y"):
    date = (datetime.today().replace(year=datetime.today().year + offset_years)).strftime(date_format)
    return date


first_names = ["Liam", "Noah", "Oliver", "William", "Elijah", "James", "Benjamin", "Lucas", "Mason", "Ethan",
               "Alexander", "Henry", "Jacob", "Michael", "Daniel", "Logan", "Jackson", "Sebastian", "Jack", "Aiden",
               "Owen", "Samuel", "Matthew", "Joseph", "Levi", "Mateo", "David", "John", "Wyatt", "Carter", "Julian",
               "Luke", "Grayson", "Isaac", "Jayden", "Theodore", "Gabriel", "Anthony", "Dylan", "Leo", "Lincoln",
               "Jaxon", "Asher", "Christopher", "Josiah", "Andrew", "Thomas", "Joshua", "Ezra", "Hudson", "Charles",
               "Caleb", "Isaiah", "Ryan", "Nathan", "Adrian", "Christian", "Maverick", "Colton", "Elias", "Aaron",
               "Eli", "Landon", "Jonathan", "Nolan", "Hunter", "Cameron", "Connor", "Santiago", "Jeremiah", "Ezekiel",
               "Angel", "Roman", "Easton", "Miles", "Robert", "Jameson", "Nicholas", "Greyson", "Cooper", "Ian",
               "Carson", "Axel", "Jaxson", "Dominic", "Leonardo", "Luca", "Austin", "Jordan", "Adam", "Xavier", "Jose",
               "Jace", "Everett", "Declan", "Evan", "Kayden", "Parker", "Wesley", "Kai", "Brayden", "Bryson", "Weston",
               "Jason", "Emmett", "Sawyer", "Silas", "Bennett", "Brooks", "Micah", "Damian", "Harrison", "Waylon",
               "Ayden", "Vincent", "Ryder", "Kingston", "Rowan", "George", "Luis", "Chase", "Cole", "Nathaniel",
               "Zachary", "Ashton", "Braxton", "Gavin", "Tyler", "Diego", "Bentley", "Amir", "Beau", "Gael", "Carlos",
               "Ryker", "Jasper", "Max", "Juan", "Ivan", "Brandon", "Jonah", "Giovanni", "Kaiden", "Myles", "Calvin",
               "Lorenzo", "Maxwell", "Jayce", "Kevin", "Legend", "Tristan", "Jesus", "Jude", "Zion", "Justin", "Maddox",
               "Abel", "King", "Camden", "Elliott", "Malachi", "Milo", "Emmanuel", "Karter", "Rhett", "Alex", "August",
               "River", "Xander", "Antonio", "Brody", "Finn", "Elliot", "Dean", "Emiliano", "Eric", "Miguel", "Arthur",
               "Matteo", "Graham", "Alan", "Nicolas", "Blake", "Thiago", "Adriel", "Victor", "Joel", "Timothy",
               "Hayden", "Judah", "Abraham", "Edward", "Messiah", "Zayden", "Theo", "Tucker", "Grant", "Richard",
               "Alejandro", "Steven", "Jesse", "Dawson", "Bryce", "Avery", "Oscar", "Patrick", "Archer", "Barrett",
               "Leon", "Colt", "Charlie", "Peter", "Kaleb", "Lukas", "Beckett", "Jeremy", "Preston", "Enzo", "Luka",
               "Andres", "Marcus", "Felix", "Mark", "Ace", "Brantley", "Atlas", "Remington", "Maximus", "Matias",
               "Walker", "Kyrie", "Griffin", "Kenneth", "Israel", "Javier", "Kyler", "Jax", "Amari", "Zane", "Emilio",
               "Knox", "Adonis", "Aidan", "Kaden", "Paul", "Omar", "Brian", "Louis", "Caden", "Maximiliano", "Holden",
               "Paxton", "Nash", "Bradley", "Bryan", "Simon", "Phoenix", "Lane", "Josue", "Colin", "Rafael", "Kyle",
               "Riley", "Jorge", "Beckham", "Cayden", "Jaden", "Emerson", "Ronan", "Karson", "Arlo", "Tobias", "Brady",
               "Clayton", "Francisco", "Zander", "Erick", "Walter", "Daxton", "Cash", "Martin", "Damien", "Dallas",
               "Cody", "Chance", "Jensen", "Finley", "Jett", "Corbin", "Kash", "Reid", "Kameron", "Andre", "Gunner",
               "Jake", "Hayes", "Manuel", "Prince", "Bodhi", "Cohen", "Sean", "Khalil", "Hendrix", "Derek", "Cristian",
               "Cruz", "Kairo", "Dante", "Atticus", "Killian", "Stephen", "Orion", "Malakai", "Ali", "Eduardo",
               "Fernando", "Anderson", "Angelo", "Spencer", "Gideon", "Mario", "Titus", "Travis", "Rylan", "Kayson",
               "Ricardo", "Tanner", "Malcolm", "Raymond", "Odin", "Cesar", "Lennox", "Joaquin", "Kane", "Wade",
               "Muhammad", "Iker", "Jaylen", "Crew", "Zayn", "Hector", "Ellis", "Leonel", "Cairo", "Garrett", "Romeo",
               "Dakota", "Edwin", "Warren", "Julius", "Major", "Donovan", "Caiden", "Tyson", "Nico", "Sergio", "Nasir",
               "Rory", "Devin", "Jaiden", "Jared", "Kason", "Malik", "Jeffrey", "Ismael", "Elian", "Marshall", "Lawson",
               "Desmond", "Winston", "Nehemiah", "Ari", "Conner", "Jay", "Kade", "Andy", "Johnny", "Jayceon", "Marco",
               "Seth", "Ibrahim", "Raiden", "Collin", "Edgar", "Erik", "Troy", "Clark", "Jaxton", "Johnathan",
               "Gregory", "Russell", "Royce", "Fabian", "Ezequiel", "Noel", "Pablo", "Cade", "Pedro", "Sullivan",
               "Trevor", "Reed", "Quinn", "Frank", "Harvey", "Princeton", "Zayne", "Matthias", "Conor", "Sterling",
               "Dax", "Grady", "Cyrus", "Gage", "Leland", "Solomon", "Emanuel", "Niko", "Ruben", "Kasen", "Mathias",
               "Kashton", "Franklin", "Remy", "Shane", "Kendrick", "Shawn", "Otto", "Armani", "Keegan", "Finnegan",
               "Memphis", "Bowen", "Dominick", "Kolton", "Jamison", "Allen", "Philip", "Tate", "Peyton", "Jase",
               "Oakley", "Rhys", "Kyson", "Adan", "Esteban", "Dalton", "Gianni", "Callum", "Sage", "Alexis", "Milan",
               "Moises", "Jonas", "Uriel", "Colson", "Marcos", "Zaiden", "Hank", "Damon", "Hugo", "Ronin", "Royal",
               "Kamden", "Dexter", "Luciano", "Alonzo", "Augustus", "Kamari", "Eden", "Roberto", "Baker", "Bruce",
               "Kian", "Albert", "Frederick", "Mohamed", "Abram", "Omari", "Porter", "Enrique", "Alijah", "Francis",
               "Leonidas", "Zachariah", "Landen", "Wilder", "Apollo", "Santino", "Tatum", "Pierce", "Forrest", "Corey",
               "Derrick", "Isaias", "Kaison", "Kieran", "Arjun", "Gunnar", "Rocco", "Emmitt", "Abdiel", "Braylen",
               "Maximilian", "Skyler", "Phillip", "Benson", "Cannon", "Deacon", "Dorian", "Asa", "Moses", "Ayaan",
               "Jayson", "Raul", "Briggs", "Armando", "Nikolai", "Cassius", "Drew", "Rodrigo", "Raphael", "Danny",
               "Conrad", "Moshe", "Zyaire", "Julio", "Casey", "Ronald", "Scott", "Callan", "Roland", "Saul", "Jalen",
               "Brycen", "Ryland", "Lawrence", "Davis", "Rowen", "Zain", "Ermias", "Jaime", "Duke", "Stetson", "Alec",
               "Yusuf", "Case", "Trenton", "Callen", "Ariel", "Jasiah", "Soren", "Dennis", "Donald", "Keith", "Izaiah",
               "Lewis", "Kylan", "Kobe", "Makai", "Rayan", "Ford", "Zaire", "Landyn", "Roy", "Bo", "Chris", "Jamari",
               "Ares", "Mohammad", "Darius", "Drake", "Tripp", "Marcelo", "Samson", "Dustin", "Layton", "Gerardo",
               "Johan", "Kaysen", "Keaton", "Reece", "Chandler", "Lucca", "Mack", "Baylor", "Kannon", "Marvin",
               "Huxley", "Nixon", "Tony", "Cason", "Mauricio", "Quentin", "Edison", "Quincy", "Ahmed", "Finnley",
               "Justice", "Taylor", "Gustavo", "Brock", "Ahmad", "Kyree", "Arturo", "Nikolas", "Boston", "Sincere",
               "Alessandro", "Braylon", "Colby", "Leonard", "Ridge", "Trey", "Aden", "Leandro", "Sam", "Uriah", "Ty",
               "Sylas", "Axton", "Issac", "Fletcher", "Julien", "Wells", "Alden", "Vihaan", "Jamir", "Valentino",
               "Shepherd", "Keanu", "Hezekiah", "Lionel", "Kohen", "Zaid", "Alberto", "Neil", "Denver", "Aarav",
               "Brendan", "Dillon", "Koda", "Sutton", "Kingsley", "Sonny", "Alfredo", "Wilson", "Harry", "Jaziel",
               "Salvador", "Cullen", "Hamza", "Dariel", "Rex", "Zeke", "Mohammed", "Nelson", "Boone", "Ricky",
               "Santana", "Cayson", "Lance", "Raylan", "Lucian", "Eliel", "Alvin", "Jagger", "Braden", "Curtis",
               "Mathew", "Jimmy", "Kareem", "Archie", "Amos", "Quinton", "Yosef", "Bodie", "Jerry", "Langston", "Axl",
               "Stanley", "Clay", "Douglas", "Layne", "Titan", "Tomas", "Houston", "Darren", "Lachlan", "Kase",
               "Korbin", "Leighton", "Joziah", "Samir", "Watson", "Colten", "Roger", "Shiloh", "Tommy", "Mitchell",
               "Azariah", "Noe", "Talon", "Deandre", "Lochlan", "Joe", "Carmelo", "Otis", "Randy", "Byron", "Chaim",
               "Lennon", "Devon", "Nathanael", "Bruno", "Aryan", "Flynn", "Vicente", "Brixton", "Kyro", "Brennan",
               "Casen", "Kenzo", "Orlando", "Castiel", "Rayden", "Ben", "Grey", "Jedidiah", "Tadeo", "Morgan",
               "Augustine", "Mekhi", "Abdullah", "Ramon", "Saint", "Emery", "Maurice", "Jefferson", "Maximo", "Koa",
               "Ray", "Jamie", "Eddie", "Guillermo", "Onyx", "Thaddeus", "Wayne", "Hassan", "Alonso", "Dash", "Elisha",
               "Jaxxon", "Rohan", "Carl", "Kelvin", "Jon", "Larry", "Reese", "Aldo", "Marcel", "Melvin", "Yousef",
               "Aron", "Kace", "Vincenzo", "Kellan", "Miller", "Jakob", "Reign", "Kellen", "Kristopher", "Ernesto",
               "Briar", "Gary", "Trace", "Joey", "Clyde", "Enoch", "Jaxx", "Crosby", "Magnus", "Fisher", "Jadiel",
               "Bronson", "Eugene", "Lee", "Brecken", "Atreus", "Madden", "Khari", "Caspian", "Ishaan", "Kristian",
               "Westley", "Hugh", "Kamryn", "Musa", "Rey", "Thatcher", "Alfred", "Emory", "Kye", "Reyansh", "Yahir",
               "Cain", "Mordechai", "Zayd", "Demetrius", "Harley", "Felipe", "Louie", "Branson", "Graysen", "Allan",
               "Kole", "Harold", "Alvaro", "Harlan", "Amias", "Brett", "Khalid", "Misael", "Westin", "Zechariah",
               "Aydin", "Kaiser", "Lian", "Bryant", "Junior", "Legacy", "Ulises", "Bellamy", "Brayan", "Kody", "Ledger",
               "Eliseo", "Gordon", "London", "Rocky", "Valentin", "Terry", "Damari", "Trent", "Bentlee", "Canaan",
               "Gatlin", "Kiaan", "Franco", "Eithan", "Idris", "Krew", "Yehuda", "Marlon", "Rodney", "Creed",
               "Salvatore", "Stefan", "Tristen", "Adrien", "Jamal", "Judson", "Camilo", "Kenny", "Nova", "Robin",
               "Rudy", "Van", "Bjorn", "Brodie", "Mac", "Jacoby", "Sekani", "Vivaan", "Blaine", "Ira", "Ameer",
               "Dominik", "Alaric", "Dane", "Jeremias", "Kyng", "Reginald", "Bobby", "Kabir", "Jairo", "Alexzander",
               "Benicio", "Vance", "Wallace", "Zavier", "Billy", "Callahan", "Dakari", "Gerald", "Turner", "Bear",
               "Jabari", "Cory", "Fox", "Harlem", "Jakari", "Jeffery", "Maxton", "Ronnie", "Yisroel", "Zakai",
               "Bridger", "Remi", "Arian", "Blaze", "Forest", "Genesis", "Jerome", "Reuben", "Wesson", "Anders",
               "Banks", "Calum", "Dayton", "Kylen", "Dangelo", "Emir", "Malakhi", "Salem", "Blaise", "Tru", "Boden",
               "Kolten", "Kylo", "Aries", "Henrik", "Kalel", "Landry", "Marcellus", "Zahir", "Lyle", "Dario", "Rene",
               "Terrance", "Xzavier", "Alfonso", "Darian", "Kylian", "Maison", "Foster", "Keenan", "Yahya", "Heath",
               "Javion", "Jericho", "Aziel", "Darwin", "Marquis", "Mylo", "Ambrose", "Anakin", "Jordy", "Juelz", "Toby",
               "Yael", "Azrael", "Brentley", "Tristian", "Bode", "Jovanni", "Santos", "Alistair", "Braydon", "Kamdyn",
               "Marc", "Mayson", "Niklaus", "Simeon", "Colter", "Davion", "Leroy", "Ayan", "Dilan", "Ephraim", "Anson",
               "Merrick", "Wes", "Will", "Jaxen", "Maxim", "Howard", "Jad", "Jesiah", "Ignacio", "Zyon", "Ahmir",
               "Jair", "Mustafa", "Jermaine", "Yadiel", "Aayan", "Dhruv", "Seven", "Stone", "Rome", "Olivia", "Emma",
               "Ava", "Sophia", "Isabella", "Charlotte", "Amelia", "Mia", "Harper", "Evelyn", "Abigail", "Emily",
               "Ella", "Elizabeth", "Camila", "Luna", "Sofia", "Avery", "Mila", "Aria", "Scarlett", "Penelope", "Layla",
               "Chloe", "Victoria", "Madison", "Eleanor", "Grace", "Nora", "Riley", "Zoey", "Hannah", "Hazel", "Lily",
               "Ellie", "Violet", "Lillian", "Zoe", "Stella", "Aurora", "Natalie", "Emilia", "Everly", "Leah", "Aubrey",
               "Willow", "Addison", "Lucy", "Audrey", "Bella", "Nova", "Brooklyn", "Paisley", "Savannah", "Claire",
               "Skylar", "Isla", "Genesis", "Naomi", "Elena", "Caroline", "Eliana", "Anna", "Maya", "Valentina", "Ruby",
               "Kennedy", "Ivy", "Ariana", "Aaliyah", "Cora", "Madelyn", "Alice", "Kinsley", "Hailey", "Gabriella",
               "Allison", "Gianna", "Serenity", "Samantha", "Sarah", "Autumn", "Quinn", "Eva", "Piper", "Sophie",
               "Sadie", "Delilah", "Josephine", "Nevaeh", "Adeline", "Arya", "Emery", "Lydia", "Clara", "Vivian",
               "Madeline", "Peyton", "Julia", "Rylee", "Brielle", "Reagan", "Natalia", "Jade", "Athena", "Maria",
               "Leilani", "Everleigh", "Liliana", "Melanie", "Mackenzie", "Hadley", "Raelynn", "Kaylee", "Rose",
               "Arianna", "Isabelle", "Melody", "Eliza", "Lyla", "Katherine", "Aubree", "Adalynn", "Kylie", "Faith",
               "Mary", "Margaret", "Ximena", "Iris", "Alexandra", "Jasmine", "Charlie", "Amaya", "Taylor", "Isabel",
               "Ashley", "Khloe", "Ryleigh", "Alexa", "Amara", "Valeria", "Andrea", "Parker", "Norah", "Eden",
               "Elliana", "Brianna", "Emersyn", "Valerie", "Anastasia", "Eloise", "Emerson", "Cecilia", "Remi",
               "Josie", "Alina", "Reese", "Bailey", "Lucia", "Adalyn", "Molly", "Ayla", "Sara", "Daisy", "London",
               "Jordyn", "Esther", "Genevieve", "Harmony", "Annabelle", "Alyssa", "Ariel", "Aliyah", "Londyn",
               "Juliana", "Morgan", "Summer", "Juliette", "Trinity", "Callie", "Sienna", "Blakely", "Alaia", "Kayla",
               "Teagan", "Alaina", "Brynlee", "Finley", "Catalina", "Sloane", "Rachel", "Lilly", "Ember", "Kimberly",
               "Juniper", "Sydney", "Arabella", "Gemma", "Jocelyn", "Freya", "June", "Lauren", "Amy", "Presley",
               "Georgia", "Journee", "Elise", "Rosalie", "Ada", "Laila", "Brooke", "Diana", "Olive", "River", "Payton",
               "Ariella", "Daniela", "Raegan", "Alayna", "Gracie", "Mya", "Blake", "Noelle", "Ana", "Leila", "Paige",
               "Lila", "Nicole", "Rowan", "Hope", "Ruth", "Alana", "Selena", "Marley", "Kamila", "Alexis", "Mckenzie",
               "Zara", "Millie", "Magnolia", "Kali", "Kehlani", "Catherine", "Maeve", "Adelyn", "Sawyer", "Elsie",
               "Lola", "Jayla", "Adriana", "Journey", "Vera", "Aspen", "Joanna", "Alivia", "Angela", "Dakota",
               "Camille", "Nyla", "Tessa", "Brooklynn", "Malia", "Makayla", "Rebecca", "Fiona", "Mariana", "Lena",
               "Julianna", "Vanessa", "Juliet", "Camilla", "Kendall", "Harley", "Cali", "Evangeline", "Mariah", "Jane",
               "Zuri", "Elaina", "Sage", "Amira", "Adaline", "Lia", "Charlee", "Delaney", "Lilah", "Miriam", "Angelina",
               "Mckenna", "Aniyah", "Phoebe", "Michelle", "Thea", "Hayden", "Maggie", "Lucille", "Amiyah", "Annie",
               "Alexandria", "Myla", "Vivienne"]

middle_names = []

last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
              "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
              "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
              "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell",
              "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart",
              "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Bailey", "Rivera", "Cooper",
              "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson",
              "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman",
              "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons",
              "Foster", "Gonzales", "Bryant ", "Alexander", "Russell", "Griffin ", "Diaz", "Hayes"]

domains = ["hotmail.com", "gmail.com", "yahoo.com", "msn.com", "outlook.com"]


def random_first_name() -> str:
    return random.choice(first_names)


def random_middle_name() -> str:
    return random.choice(middle_names)


def random_last_name() -> str:
    return random.choice(last_names)


def random_domain() -> str:
    return random.choice(domains)


class ClientData:

    def __init__(self):
        self.first_name = random_first_name()
        self.last_name = random_last_name()
        self.email = f"{self.first_name}.{self.last_name}{random_number(3)}@{random_domain()}".lower()


def test_stuff(page):
    items = []
    page.goto("https://rong-chang.com/namesdict/100_last_names.htm")
    table_items = page.querySelectorAll("//table//tr/td/font//font/b/a")
    for item in table_items:
        items.append(item.textContent())
        print(f"\"{item.textContent()}\", ")


def test_more_stuff(page):
    print(f"{random_first_name()} {random_last_name()}")


