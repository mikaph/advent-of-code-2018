with open('input4', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()


sorted_input = []
timed_actions = {}

for line in puzzle_input:
    timed_actions.update({line[6:8] + line[9:11] + line[12:14] + line[15:17]: line})

for key in sorted(timed_actions):
    sorted_input.append(timed_actions[key])


class Guard:
    def __init__(self):
        self.sleeping = [0 for i in range(60)]
        self.last_sleep_time = -1
        self.last_awake_time = -1

    def sleep(self, time):
        self.last_sleep_time = time

    def wake_up(self, time):
        self.last_awake_time = time
        self.inc_sleeping(self.last_sleep_time, time)

    def inc_sleeping(self, start, end):
        for i in range(start, end):
            self.sleeping[i] += 1

    def get_time_sleeping(self):
        result = 0
        for i in self.sleeping:
            result += i

        return result

    def get_most_sleepy_minute(self):
        return self.sleeping.index(max(self.sleeping))

    def get_most_sleep_on_minute(self):
        return self.sleeping[self.get_most_sleepy_minute()]


guards = {}
active_guard = -1

for line in sorted_input:
    if '#' in line:
        l2 = line[line.find('#')+1:]
        active_guard = int(l2[:l2.find(' ')])
        if active_guard not in guards:
            guards.update({active_guard: Guard()})

    elif "falls" in line:
        guards[active_guard].sleep(int(line[line.find(':')+1:line.find(']')]))

    elif "wakes" in line:
        guards[active_guard].wake_up(int(line[line.find(':')+1:line.find(']')]))


guard_sleeptimes = {}
for guard in guards:
    guard_sleeptimes.update({guard: guards[guard].get_time_sleeping()})

the_guard = max(guard_sleeptimes, key=guard_sleeptimes.get)
sleepiest_minute = guards[the_guard].get_most_sleepy_minute()

print("answer: " + str(the_guard * sleepiest_minute))

sleepiest_minutes = {}

for guard in guards:
    sleepiest_minutes.update({guards[guard].get_most_sleep_on_minute(): guard})

the_guard2 = sleepiest_minutes[max(sleepiest_minutes)]
sleepiest_minute2 = guards[the_guard2].get_most_sleepy_minute()

print("answer2: " + str(the_guard2 * sleepiest_minute2))
