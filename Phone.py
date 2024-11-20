# 1. Create 2 instances of the iPhone.
# 2. Change iPhone names through set_name()
# 3. Send a iMessage from phone1 to phone2
# 4. phone2 should be able to check messages. Print the messages on screen.
# Solution
class iPhone:
    def __init__(self, model, color, name, storage, os_version):
        self.model = model
        self.color = color
        self.name = name
        self.storage = storage
        self.os_version = os_version
        self.messages = []

    def set_name(self, new_name):
        self.name = new_name

    def airdrop(self, target_phone, file_name): # This feature is done during the class so I just add it in
        if isinstance(target_phone, iPhone):
            if self.os_version == target_phone.os_version:
                print(f"Airdropping '{file_name}' from {self.name} to {target_phone.name}.")
            else:
                print("Airdrop failed: OS versions are incompatible.")
        else:
            print("Airdrop failed: Target device is not an iPhone.")

    def iMessage(self, target_phone, message):
        if isinstance(target_phone, iPhone):
            target_phone.messages.append((self.name, message))
            print(f"Message sent from {self.name} to {target_phone.name}: {message}")
        else:
            print("iMessage failed: Target device is not an iPhone.")

    def check_messages(self):
        if len(self.messages) > 0:
            print(f"Messages received by {self.name}:")
            for sender, message in self.messages:
                print(f"From {sender}: {message}")
        else:
            print(f"No messages received by {self.name}.")


iPhone_1 = iPhone("iPhone 16 Pro Max", "Black", "Steven's iPhone", "512GB", "ios 18.1")
iPhone_2 = iPhone("iPhone 13 Pro Max", "White", "Joey's iPhone", "256GB", "ios 17.6")

iPhone_1.set_name("Steven's New iPhone")
iPhone_2.set_name("Joey's Old iPhone")
print(iPhone_1.name)
print(iPhone_2.name)

iPhone_1.airdrop(iPhone_2, "pictures taken on Monday")

iPhone_1.iMessage(iPhone_2, "Joey, let's go to the park this weekend!")
iPhone_2.iMessage(iPhone_1, "Sure, Steven! What time?")

iPhone_1.check_messages()
iPhone_2.check_messages()