class player:
  def __init__(self, name):
    self.name = name
    self.life = 8000
    self.start_msg = True
  
  def string(self):
    if self.life <= 0:
      return f"{self.name}の残りライフが0になりました。負けです。"
    return f"{self.name}の残りライフは{self.life}です。"
  
  def diff(self, num):
    self.life = self.life - num
    return f"{self.name}のライフを{num}引きました。\n{self.string()}"
  
  def half(self):
    self.life = -(-self.life // 2)
    return f"{self.name}のライフを半分にしました。\n{self.string()}"