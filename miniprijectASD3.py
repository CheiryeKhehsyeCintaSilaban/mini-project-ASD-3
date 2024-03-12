class Node:
    def __init__(self, id_gereja, nama, alamat, tahun_berdiri):
        self.id_gereja = id_gereja
        self.nama = nama
        self.alamat = alamat
        self.tahun_berdiri = tahun_berdiri
        self.next = None

class GerejaLinkedList:
    def __init__(self):
        self.head = None

    def create_data(self, id_gereja, nama, alamat, tahun_berdiri):
        new_node = Node(id_gereja, nama, alamat, tahun_berdiri)
        new_node.next = self.head
        self.head = new_node
        print(f'Data gereja dengan ID {id_gereja} berhasil ditambahkan.')

    def read_data(self, id_gereja=None):
        current = self.head

        if id_gereja:
            while current:
                if current.id_gereja == id_gereja:
                    print(f'Data gereja dengan ID {id_gereja}:')
                    print(f'ID Gereja: {current.id_gereja}')
                    print(f'Nama: {current.nama}')
                    print(f'Alamat: {current.alamat}')
                    print(f'Tahun Berdiri: {current.tahun_berdiri}')
                    return
                current = current.next
            print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')
        else:
            print('Data seluruh gereja:')
            while current:
                print(f'ID Gereja: {current.id_gereja}')
                print(f'Nama: {current.nama}')
                print(f'Alamat: {current.alamat}')
                print(f'Tahun Berdiri: {current.tahun_berdiri}')
                print()
                current = current.next

    def update_data(self, id_gereja, field, value):
        current = self.head

        while current:
            if current.id_gereja == id_gereja:
                if hasattr(current, field):
                    setattr(current, field, value)
                    print(f'Data {field} gereja dengan ID {id_gereja} berhasil diperbarui.')
                    return
                else:
                    print(f'Field {field} tidak valid.')
                    return
            current = current.next

        print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')

    def delete_data(self):
        if self.head:
            deleted_node = self.head
            self.head = self.head.next
            print(f'Data gereja dengan ID {deleted_node.id_gereja} berhasil dihapus.')
        else:
            print('Tidak ada data gereja untuk dihapus.')

    def quick_sort(self):
        self.head = self._quick_sort(self.head)

    def _quick_sort(self, start):
        if start is None or start.next is None:
            return start

        pivot = start.id_gereja
        lesser_head = None
        equal_head = None
        greater_head = None
        current = start

        while current:
            if current.id_gereja < pivot:
                if lesser_head is None:
                    lesser_head = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                else:
                    lesser_head.next = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
            elif current.id_gereja == pivot:
                if equal_head is None:
                    equal_head = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                else:
                    equal_head.next = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
            else:
                if greater_head is None:
                    greater_head = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                else:
                    greater_head.next = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)

            current = current.next

        sorted_head = self._quick_sort(lesser_head)
        if equal_head:
            if sorted_head:
                current = sorted_head
                while current.next:
                    current = current.next
                current.next = equal_head
            else:
                sorted_head = equal_head

        greater_sorted = self._quick_sort(greater_head)
        if sorted_head:
            current = sorted_head
            while current.next:
                current = current.next
            current.next = greater_sorted
        else:
            sorted_head = greater_sorted

        return sorted_head


def main():
    gereja_list = GerejaLinkedList()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Gereja")
        print("2. Tampilkan Data Gereja")
        print("3. Perbarui Data Gereja")
        print("4. Hapus Data Gereja")
        print("5. urutkan data gereja")
        print("6. Keluar")

        pilihan = input("Silakan masukkan pilihan anda: ")

        if pilihan == '1':
            id_gereja = input("Masukkan ID gereja: ")
            nama = input("Masukkan nama gereja: ")
            alamat = input("Masukkan alamat lengkap gereja: ")
            tahun_berdiri = input("Masukkan tahun berdiri gereja tersebut: ")
            gereja_list.create_data(id_gereja, nama, alamat, tahun_berdiri)

        elif pilihan == '2':
            id_gereja = input("Masukkan ID Gereja untuk menampilkan produk (kosongkan untuk semua): ")
            gereja_list.read_data(id_gereja)

        elif pilihan == '3':
            id_gereja = input("Masukkan ID Gereja: ")
            field = input("Masukkan Nama Field yang Ingin Diperbarui: ")
            value = input("Masukkan Nilai Baru: ")
            gereja_list.update_data(id_gereja, field, value)

        elif pilihan == '4':
            gereja_list.delete_data()

        elif pilihan == '5':
            gereja_list.quick_sort()
            print("Data gereja berhasil diurutkan secara ascending berdasarkan ID.")

        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih ulang")


if __name__ == "__main__":
    main()