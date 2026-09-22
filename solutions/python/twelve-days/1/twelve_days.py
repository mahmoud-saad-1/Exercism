
DAYS = (
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
)

GIFTS = (
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, and ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, "
)

def recite(start_verse, end_verse):
    result = []
    
    
    for v in range(start_verse, end_verse + 1):
        # Indexing into your DAYS tuple dynamically
        day_text = DAYS[v - 1]
        joined_gifts = "".join(GIFTS[v - 1 :: -1])
        
        verse_str = f"On the {day_text} day of Christmas my true love gave to me: {joined_gifts}"
        
        
        result.append(verse_str)
        
    return result