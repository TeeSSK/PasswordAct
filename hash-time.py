import hashlib
import time


def hashWithSha1(word):
    m = hashlib.sha1(word.encode()).hexdigest()
    return m


def main():
    print("Hacking Passwords")
    n = 10
    list_elapsed_time = []
    for i in range(n):
        start_time_np = time.time()
        hashSha1 = str(hashWithSha1(
            "123456lsajdflkjskal;kfjlsdjvoiknsdoa;nv;lakskljdskflgjobiesobnoslkfbldskjfbl;jdslfbjoesijfrboijsodij"))
        end_time_np = time.time()
        elapsed_time = end_time_np - start_time_np
        list_elapsed_time.append(elapsed_time)
    average_time = sum(list_elapsed_time) / n
    print("Average time: " + str(average_time))


if __name__ == '__main__':
    main()

#
