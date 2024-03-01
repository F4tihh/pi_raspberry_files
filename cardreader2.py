from time import sleep, time

def read_process():
    # Resim kimlik kartları listesi
    resim_id_listesi = [1, 2, 3, 4, 5, 6, 7]

    try:
        reads = dict()
        for i in range(5):
            resim_id = resim_id_listesi[i]
            reads[i] = resim_id
        return reads

    except KeyboardInterrupt:
        raise

if __name__ == "__main__":
    reads = read_process()
    print("reads:", reads)
    
