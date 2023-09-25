def atusername(self, split):
    if len(split) != 2:
        print("Usage: @username [username]")
        return self
    self.player.name = split[1]
    return self


def emote(self, split):
    if len(split) < 2:
        print("Usage: emote [kicks you in the shins.]")
        return self
    print(f"{self.player.name} {' '.join(split[1:])}")
    return self
