import random
from pyfiglet import Figlet


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$&_+-*/=<>^%$"

use_for = lower_case + upper_case + number + symbols


length_for_pass = 12  #

password = [random.choice(use_for) for _ in range(length_for_pass)]


random.shuffle(password)


password = "".join(password)


print(f"\033[91mVotre mot de passe est : {password}\033[0m")

print("\npassword generate stopped.")
