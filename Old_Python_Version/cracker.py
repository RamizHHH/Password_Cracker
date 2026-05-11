from Old_Python_Version.hash_util import hashPassword
import time
from multiprocessing import Pool, cpu_count
from Old_Python_Version.rules import apply_rule
import numpy as np
import bcrypt
import os

def dict_attack(wordlist, hashedPassword, hash_type, rule_type):


    start_time = time.time()

    attempts = 0


    candidate_stream = (
        (v, hashedPassword, hash_type)
        for v in readWordList(wordlist, hash_type, rule_type)
    )

    speeds = []

    with Pool(cpu_count()) as pool:

            results = pool.imap_unordered(
                checkPassword, candidate_stream, chunksize=1000
            )
            
            for result in results:

                attempts += 1
                
                if result:

                    elapsedTime = time.time() - start_time

                    print(f"Password is {result}\n")

                    print(f"[+] Attempts: {attempts}\n")
                    print(f"[+] Elapsed Time: {elapsedTime}\n")
                    print(f"[+] Time: {elapsedTime:.2f} seconds\n")
                    print(f"[+] Average hashes / sec: {np.mean(speeds):.2f}\n")
                    print(f"[+] CPU Cores: {os.cpu_count()}\n")

                    pool.terminate()

                    return

                if attempts % 100 == 0:

                    elapsedTime = time.time() - start_time

                    speed = attempts / elapsedTime

                    speeds.append(speed)

                    print(f"Tried: {attempts} | " f"Speed: {speed:.2f} hashes / sec")

    print("Password not found")


def checkPassword(args):
    variation, target_hash, hash_type = args
    

    if hash_type == "bcrypt":
        if bcrypt.checkpw(variation.encode(), target_hash.encode()):
            return variation
        return None
        
        
    hash_value = hashPassword(variation, hash_type)
    
    if hash_value == target_hash:
        return variation
    
    return None

def readWordList(wordList, hash_type, rule_type):
     with open(wordList, "r", encoding='latin-1') as wl:
         for line in wl:

            word = line.strip()

            variations = apply_rule(word, rule_type)

            for variation in variations:

                hash_type = hash_type.lower()

                yield variation