# ATATvI
## ATATvI: Algorithmic Tonal Analysis of Text vs Intent

## Team MARV - Mid Term Project Pitch

### Background
As team MARV we identify strongly with Marvin from The Hitchhiker's Guide to the Galaxy novel by Douglas Adams. Marvin is known in the Hitchhikers as Marvin the Paranoid Android (shout out to Radiohead) and sometimes as Marvin the Depressed Robot. For sure Marvin has a slight predisposition that tends towards negative self talk. However, we feel that much of Marvin’s outlook on life is caused by the language people use around him and the words they direct to him.

Language matters. Our use of language matters. The words we use and the way we use then in context has a direct impact on organizations and an effect on individuals and communities. As Code Fellows students and soon to be Alumni we hold fast to the values and standards we have been taught as they relate to inclusivity, diversity and accessibility for all. Words are important and we would like to create a tool that helps individuals and organizations identify when their words may tend towards gender bias, exclusivity and/or negativity.


### Problem Domain
Sometimes use of negative and/or inflammatory language is intentional and designed to belittle or otherwise harm individuals and communities. However, much of the time the use of such language is accidental and mostly comes down to a lack of awareness, an oversight and/or unawareness of cultural context. In such situations it would be helpful to have a tool that could check the words used in a document, audio file or film clip and validate whether any of the language used could be classed as damaging to certain people groups.


### Proposed Solution
Utilize Watson tone analysis (https://www.ibm.com/watson/services/tone-analyzer/) and teach our implemented model to learn about and then identify language that could be considered negative and/or inflammatory. Given that Watson returns a collection of potential tones found in a document, we will take those suggestions and compare them to public platforms and return the difference.

### Minimal Viable Product
Be able to read a transcript and identify where there is a disparity between tone and the intended message.  
Provide a high level comparison of the discrepancies to the user.


### Stretch Goals

*Train our own Natural Language Processor using the Karis API to meet specific needs, enumerated below: 

*Be able to analyze social media (Tweets etc.) for potentially gender biased words.

*Be able to analyze audio files for potentially gender biased words.

*Be able to analyze movie files for potentially gender biased words.

*Be able to analyze transcripts, audio files or movie files for words that do not promote diversity.

*Be able to analyze transcripts, audio files or movie files for words that do not promote inclusivity.

*Be able to analyze transcripts, audio files or movie files for words that do not promote growth mindset.

*Be able to analyze transcripts, audio files or movie files for words that do not promote accessibility for as many individuals and people groups as possible.
