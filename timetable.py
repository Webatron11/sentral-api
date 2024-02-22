class Lesson:
	def __init__(self, room, subject, teachers):
		self.room = room
		self.subject = subject
		self.teacher = teachers


class Period:
	def __init__(self, lesson: Lesson, start, end, number: int):
		self.lesson = lesson
		self.start = start
		self.end = end
		self.number = number


class Periods:
	def __init__(self):
		self.periods = [
			Period(Lesson("", "", ""), "", "", 0),
			Period(Lesson("", "", ""), "", "", 1),
			Period(Lesson("", "", ""), "", "", 2),
			Period(Lesson("", "", ""), "", "", 3),
			Period(Lesson("", "", ""), "", "", 4),
			Period(Lesson("", "", ""), "", "", 5),
			Period(Lesson("", "", ""), "", "", 6),
			Period(Lesson("", "", ""), "", "", 7)
		]

	def updateperiod(self, period: Period):
		self.periods[period.number] = period


class Day:
	def __init__(self, periods: Periods, date):
		self.periods = periods
		self.date = date


class Days:
	def __init__(self):
		self.days = [
			Day(Periods(), ""),
			Day(Periods(), ""),
			Day(Periods(), ""),
			Day(Periods(), ""),
			Day(Periods(), "")]

	def updateday(self, day: Day, number: int):
		self.days[int(number)-1] = day


class Week:
	def __init__(self, days: Days, letter):
		self.days = days
		self.letter = letter


class Fornight:
	def __init__(self, weeka: Week, weekb: Week):
		self.weeka = weeka
		self.weekb = weekb
