# Project Proposal
## The Big Idea
This project creates a bot to generate a list of recipes based off of the ingredients that you have in your fridge. The bot acts as a cooking assistance who guides you to what you are cooking for your next meal. If successful, the goal of this project is to help users decrease food waste and to bring in more variety in their day to day meals. The ability to return a list of recipes from a list of ingredients is my minimun viable product. However, if time allows, I hope to include preferences in macronutrient intakes (%Carbs, %Fat, %Protein) to create a weekly meal plan for the user, which would include Breakfast, Lunch, and Dinner. 

## Learning Objectives
My goal for this project is to further my studies with utizling APIs. I think that this project will be great practice for that. 

## Implementaion Plan
Currently, I am utizling the Spoonacular API to pull recipes and ingredient lists. However, I still need to do more research on recipe APIs to find the best match for my project's objective. 

PART 1: In order to generate a list of recipes. I plan to ask the users to input their ingredients. After, I will do a comparison. So if x ingredient is in recipe's ingredients list, this recipe will be returned. This continues for all the recipes and will be sorted by the most similar list of ingredients and the amount that the recipe uses. (more the better)

PART 2: To generate the list of recipes that matches the macronutrience ratios, I will need to look for another API to pull the grams of protein, carbs, and fat in each serving per recipe. I will then compare the user's input to the recipe's data and find the recipes that includes the highest match. 

PART 3: To generate a meal plan, I plan to use random to randomly select from the recipes found prior based on ingredients list and macros and split it up, so they have a balanced diet on the daily. I think that some recipes might not work for breakfast, but might work for dinner. So I will look into whether or not there is data in each recipe that specifies if it is a breakfast, lunch, or dinner. 

## Project Schedule
As of right now, I have 3 weeks for this project:
This weekend (4/6-4/8): find fitting API/ familarize myself with the data
week 1 
4/9-4/15: execution of part 1 of the plan. (generate a list of recipes based off of user's ingredients)
week 2 
4/16- 4/22: execution of part 2 of the plan. (generate a list of recipes based off of user's ingredients + macro nutrients needs)
week 3 
4/23 - 4/26: execution of part 3 of the plan. (organize the list of recipes to a meal plan schedule)
4/26 - 4/28: website design + final details
4/29: Project Due Date

## Collaborative Plan 
I plan to work on this individually. However, I may ask other peope for their opinions to improve my project. 

## Risks and Limitations
My greatest limitation is the API at this moment. The API that I found only allows 150 requests per week. This creates a huge limitation on the amount of tests that I can have.

## Additional Course Content
What topics do you believe will be beneficial to your project?