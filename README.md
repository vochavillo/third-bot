# third-bot

How to this:
  import bot
  response = bot.ask_question
  if response == 'Y':
    bot.bot()


The cost of housing in the Bay Area is increasing. With the calls for more affordable housing, I wanted to look at whether the affordable housing units in San Francisco fell under the city's inclusionary housing program that began in 1992. The inclusionary housing program warranted that any housing development of 10 or more housing units would have to set aside a portion of all total units to be affordable. The plan was to find any matches between the affordable housing dataset and the inclusionary housing dataset. Across the information provided, I thought to match by location, assuming that, if there was a match, the latitude and longitude of a housing development in one dataset would reflect the same coordinates in the other dataset. Interestingly enough, there were no matches. And I wouldn't attribute this to the city's failure to build more affordable housing or all housing developers opting to pay a fee to avoid setting aside any affordable housing units in their projects, at least without further investigation. There are several explanations to the no-match results. One may be that the latitude and longitude coordinates were not of equal precision and uniformly entered across the two datasets. Another may be that the either dataset did not capture any of the housing units that were built prior to a certain date--I tried to find out the earliest housing development in both datasets, to understand how far the data went, but one dataset provided no 'date' information.

Had there been a match, I would a Google map would have been provided with the pins visualizing where these housing units would be located in the city. A function that would produce this Google map URL is included in the program but ended up not being called because there were no matches between the affordable housing dataset and the inclusionary housing dataset.

This project was especially enlightening around the necessary clean-up and transformation that are necessary when working with multiple datasets. It was my premature assumption that because the two datasets were both put together by the city of San Francisco that their data-entry staff would have standardized the information collected and the way that data was inputted. I was mistaken.

For example, in extracting the location of each entry, in one dataset the location was given in terms of latitude and longitude--both as part of one continuous string--while the other dataset provided the location as a string that included not only latitude and longitude but also the street address. To be able to compare apples to apples, so to speak, I needed to perform a little more processing of the string. Of course, the easier option would have been to have had the latitude and longitude data entered as two separate values under two different columns.

Other minor necessity, after receiving multiple errors messages, was that in order to compare two pairs of latitude and longitude, I had to convert the string to floats. This was easy enough but I did sit for a good two minutes wonderful why two latitude-longitude pairs were being saved as having a perfect match between all values when the longitudes didn't match. The original matching functions were comparing strings rather than floats. As far as I could tell, matching by latitude and longitude was the best characteristic on which to compare the datasets.

Given the underwhelming result of the printed line, "There are no recorded housing projects in..." I decided to include a series of print line statements that provide the number of inclusionary housing projects at different progress stages, as well as information on the earliest project. This gives the reader a sense of the length of time the inclusionary requirement has been around.

Looking back, these two datasets may not have been the best datasets to compare. Assuming that the datasets were complete and that they were matched appropriately, then there being no matched could mean that all housing developments have successfully avoided reserving a portion of their units for affordable housing units, or that no affordable housing units were built after 1992. Ways to confirm this? If there was a dataset that contained those housing developers who paid the inclusionary housing fee.
