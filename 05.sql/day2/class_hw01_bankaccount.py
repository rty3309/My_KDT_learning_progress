# 파이썬 클래스 활용 과제 1
# KDT 12기 이재헌

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__balance = 0

    def deposit(self, amount):
        if amount % 10000 != 0:
            print("[입력 오류] 10000원 단위로 다시 입력하세요.")
            return
        self.__balance += amount
        print(f"{amount:,} 원 입금: 통장 잔액: {self.__balance:,}")

    def withdraw(self, amount):
        if amount % 10000 != 0:
            print("[입력 오류] 10000원 단위로 다시 입력하세요.")
            return
        if self.__balance < amount:
            print(f"통장 잔액이 부족합니다. 통장 잔액: {self.__balance:,}")
            return
        self.__balance -= amount
        print(f"{amount:,} 원 출금, 통장 잔액: {self.__balance:,}")

    def print_balance(self):
        print(f"{self.name}, 잔액: {self.__balance:,}원")

    def run(self):
        while True:
            print("--------------------")
            print(f"{self.name}")
            print("1. 입금")
            print("2. 출금")
            print("3. 조회")
            print("4. 종료")
            print("--------------------")

            try:
                menu = int(input("메뉴 선택: "))
            except ValueError:
                print("[입력 오류] 숫자를 입력하세요.")
                continue

            if menu == 1:
                try:
                    amount = int(input("입금할 금액을 10000원 단위로 입력하세요: "))
                    self.deposit(amount)
                except ValueError:
                    print("[입력 오류] 숫자를 입력하세요.")

            elif menu == 2:
                try:
                    amount = int(input("출금할 금액을 10000원 단위로 입력하세요: "))
                    self.withdraw(amount)
                except ValueError:
                    print("[입력 오류] 숫자를 입력하세요.")

            elif menu == 3:
                self.print_balance()

            elif menu == 4:
                print("프로그램을 종료합니다.")
                break
            
            else:
                print("잘못된 메뉴 선택입니다. 다시 입력하세요.")

def main():
    account = BankAccount("KDT 은행")
    account.run()

if __name__ == "__main__":
    main()