import random
import math
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

GAMMA = 0.9
LAMBDA = 0.5

class Model:
   def __init__(self, states, actions, batch_size):
      self.num_states = states
      self.num_actions = actions
      self.batch_size = batch_size
      # Holders
      self.states = None
      self.actions = None
      # outs
      self.logits = None
      self.optimizer = None
      self.var_init = None
      # Setup
      self.define_model()

   def define_model(self):
      self.states = tf.placeholder(shape=[None, self.num_states], dtype=tf.float32)
      self.q_s_a = tf.placeholder(shape=[None, self.num_actions], dtype=tf.float32)
      # Create hidden layers
      fc1 = tf.layers.dense(self.states, 50, activation=tf.nn.relu)
      fc2 = tf.layers.dense(fc1, 50, activation=tf.nn.relu)
      self.logits = tf.layers.dense(fc2, self.num_actions)
      loss = tf.losses.mean_squared_error(self.q_s_a, self.logits)
      self.optimizer = tf.train.AdamOptimizer().minimize(loss)
      self.var_init = tf.global_variables_initializer()

   def predict_one(self, state, moves, sess):
      return sess.run(self.logits, feed_dict={self.states: np.reshape(state, [1, self.num_states]), self.actions: moves})

   def predict_batch(self, states, sess):
      return sess.run(self.logits, feed_dict={self.states: states})

   def train_batch(self, sess, x_batch, y_batch):
      sess.run(self.optimizer, feed_dict={self.states: x_batch, self.q_s_a: y_batch})


class Memory:
   def __init__(self, max):
      self.max_memory = max
      self.samples = []

   def add_sample(self, sample):
      self.samples = self.samples + [sample]
      if len(self.samples) > self.max_memory:
         self.samples.pop(0)

   def sample(self, cnt):
      if cnt > len(self.samples):
         return random.sample(self.samples, len(self.samples))
      else:
         return random.sample(self.samples, cnt)


class TicTacToe:

   def __init__(self):
      self.gen_baord()
      self.playing = 1
      self.movesMade = 0
      self.useAI = False
      self.winner = 0

   def gen_baord(self):
      self.board = [0,0,0,0,0,0,0,0,0]
      return True
   
   def display(self):
      position = 0
      divisorLine = "---|---|---"
      for line in range(1,6,1):
         if line % 2 == 1:
            lineStr = ""
            for pos in range(position,position + 3,1):
               if self.board[pos] == 1:
                  lineStr = lineStr + " X "
               elif self.board[pos] == 2:
                  lineStr = lineStr + " O "
               else: # print position if is not taken
                  lineStr = lineStr + " " + str(pos) + " "
               if pos < position + 2: # check if not last val
                  lineStr = lineStr + "|"
            position = position + 3
            print(lineStr)
         else:
            print(divisorLine)
      return True # ran successfully to finish

   def toggle_ai(self):
      self.useAI = False if self.useAI else True
      return True

   def duplicate(self):
      dup = TicTacToe()
      dup.board = list(self.board)
      dup.playing = self.playing
      dup.movesMade = self.movesMade
      dup.useAI = self.useAI
      return dup

   def generate_move(self):
      moves = self.get_open_moves()
      if len(moves) == 1:
         return moves[0]
      results = []
      for v in moves:
         results = results + [self.simulate_move(v, False)]
      ind = 0
      for v in moves:
         res = self.simulate_move(v, True)
         if res == self.playing:
            results[ind] = res
         ind = ind + 1
      ind = 0
      nonLoss = []
      enemy = 2 if self.playing == 1 else 1
      for r in results:
         if r == self.playing:
            return moves[ind]
         elif r == enemy:
            nonLoss = nonLoss + [moves[ind]]
         ind = ind + 1
      if len(nonLoss) > 0:
         return nonLoss[0]
      return moves[random.randint(0, len(moves)-1)]

   def simulate_move(self, pos, playAsSelf):
      new = self.duplicate()
      if not playAsSelf:
         new.change_turn()
      new.toggle_ai()
      r = new.process_turn(pos)[1]
      return r

   def get_open_moves(self):
      avail = []
      pos = 0
      for v in self.board:
         if v == 0:
            avail = avail + [pos]
         pos = pos + 1
      return avail


   def change_turn(self):
      self.playing = 2 if self.playing == 1 else 1
      return True

   def validate_pos(self, pos):
      if pos < 0 or pos > 8:
         return False
      return True

   def process_turn(self, pos):
      done = False
      if self.make_move(pos):
         self.movesMade = self.movesMade + 1
         win = self.check_win(pos)
         self.change_turn()
         if self.useAI and self.playing == 2 and win == 0 and self.movesMade <= 8:
            move = self.generate_move()
            if self.process_turn(move)[2]:
               win = self.playing
               done = True
         if win <= 0 and self.movesMade > 8:
            self.winner = -1
            done = True
         elif win != 0:
            self.winner = win
            done = True
         return [self.winner] + self.board, 0, done
      return [-2] + self.board, 0, False

   def make_move(self, pos):
      if self.validate_pos(pos):
         if self.check_move(pos):
            self.board[pos] = self.playing
            return True
      return False

   def check_move(self, pos):
      if self.board[pos] == 0:
         return True
      return False

   def check_win(self, pos):
      x = pos % 3
      y = int((pos - x)/3)
      # Check vertical
      if self.board[0+x] == self.board[3+x] == self.board[6+x]:
         return self.playing
      # Check Horizontal
      if self.board[y*3] == self.board[y*3+1] == self.board[y*3+2]:
         return self.playing
      # Check Diagonal (if exists)
      if self.board[4] == self.board[0] == self.board[8] != 0:
         return self.playing
      if self.board[4] == self.board[2] == self.board[6] != 0:
         return self.playing
      return 0

   def reset(self):
      self.gen_baord()
      self.playing = 1
      self.movesMade = 0
      self.useAI = False
      self.winner = 0
      return [0] + self.board

# def main():
#    game = TicTacToe()
#    game.toggle_ai()
#    game.display()
#    while True:
#       move = input()
#       res = game.process_turn(int(move))
#       try:
#          pass
#       except:
#          print("ERR: The position input was invalid")
#          continue
#       game.display()
#       if not res[0]:
#          print("ERR: The move could not be performed")
#       if res[1] > 0:
#          print("Player " + str(res[1]) + " has won!")
#          break
#       elif res[1] == -1:
#          print("DRAW!")
#          break
#    return True

'''
STATES
0 -> in play
1 -> Win
2 -> Loss
-1 -> Draw
'''

class Runner:
   def __init__(self, sess, model : Model, env : TicTacToe, memory : Memory, max_eps, min_eps, decay, render=True):
      self.sess = sess
      self.env = env
      self.model = model
      self.memory = memory
      self.render = render
      self.max_eps = max_eps
      self.min_eps = min_eps
      self.decay = decay
      self.eps = self.max_eps
      self.steps = 0
      self.rewards = []
      self.turns = []

   def run(self):
      state = self.env.reset()
      self.env.toggle_ai()
      total_reward = 0
      while True:
         if self.render:
            self.env.display()
         action = self.choose_action(state, self.env.get_open_moves())
         next_state, reward, done = self.env.process_turn(action)

         if next_state[0] == 0:
            reward += 10
         elif next_state[0] == 1:
            reward += 1000*(5-self.steps)
         elif next_state[0] == 2:
            reward -= 1000
         else:
            reward = 0

         if done:
            next_state = None

         self.memory.add_sample((state, action, reward, next_state))
         self.replay()
         
         # Decay epsilon
         self.steps += 1
         self.eps = self.min_eps + (self.max_eps - self.min_eps) * math.exp(-LAMBDA*self.steps)

         state = next_state
         total_reward += reward

         if done:
            self.rewards.append(total_reward)
            self.turns.append(self.steps)
            break
      print("FINAL")
      self.env.display()
      print("Step {}, Total Reward: {}, Eps: {}".format(self.steps, total_reward, self.eps))
      self.steps = 0
      return True


   def choose_action(self, state, moves):
      if random.random() < self.eps:
         return moves[random.randint(0, len(moves))]
      else:
         return np.argmax(self.model.predict_one(state, moves, self.sess))

   def replay(self):
      batch = self.memory.sample(self.model.batch_size)
      states = np.array([val[0] for val in batch])
      next_states = np.array([(np.zeros(self.model.num_states) if val[3] is None else val[3]) for val in batch])
      # Predict Q(s, a)
      q_s_a = self.model.predict_batch(states, self.sess)
      # Predict Q(s', a') -> for dat algebra below
      q_s_a_d = self.model.predict_batch(next_states, self.sess)
      # Make some training stuff
      x = np.zeros((len(batch), self.model.num_states))
      y = np.zeros((len(batch), self.model.num_actions))
      for i, b in enumerate(batch):
         state, action, reward, next_state = b[0], b[1], b[2], b[3]
         # Get q
         current_q = q_s_a[i]
         # Update 
         if next_state is None:
            current_q[action] = reward
         else:
            current_q[action] = reward + GAMMA * np.amax(q_s_a_d[i])
         x[i] = state[0]
         y[i] = current_q
      self.model.train_batch(self.sess, x, y)

if __name__ == "__main__":
   env = TicTacToe()

   num_states = 10
   num_actions = 9

   model = Model(num_states, num_actions, 55)
   mem = Memory(50000)

   with tf.Session() as sess:
      sess.run(model.var_init)
      saver = tf.train.Saver()
      saver.restore(sess, "./tmp/ttt_mi.ckpt")
      gr = Runner(sess, model, env, mem, 1, 0.1, LAMBDA)
      num_episodes = 10
      cnt = 0
      while cnt < num_episodes:
         if (cnt % 10 == 0):
            print("Episode {} of {}".format(cnt+1, num_episodes))
         gr.run()
         cnt += 1
      save_path = saver.save(sess, "./tmp/ttt_mi.ckpt")
      print("Model Saved to: %s" % save_path)
      plt.plot(gr.rewards)
      plt.show()
      plt.close("all")
      plt.plot(gr.turns)
      plt.show()