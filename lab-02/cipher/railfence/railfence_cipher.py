class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encr(self, plaint_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1

        for char in plaint_text:
            rails[rail_index].append(char)
            rail_index += direction

            if rail_index == 0 or rail_index == num_rails - 1:
                direction = -direction

        cipher_text = "".join("".join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decr(self, cipher_text, num_rails):
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            rail_index += direction

            if rail_index == 0 or rail_index == num_rails - 1:
                direction = -direction

        rails = [""] * num_rails
        index = 0

        for char in cipher_text:
            rails[index] += char
            index += 1
            if index == num_rails:
                index = num_rails - 2
                direction = -1
            elif index == -1:
                index = 1
                direction = 1

        plain_text = "".join(rails)
        return plain_text
