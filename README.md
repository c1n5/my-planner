
# MyPlanner Crew

## **Overview**  
The **Meal Planning Multi-Agent System (MAS)** is designed to create personalized weekly meal plans and optimized shopping lists tailored to user preferences, dietary requirements, and health goals. Built using the **CrewAI framework**, this system combines the expertise of three agents—Dietary Analyst, Menu Planner, and Shopping List Optimizer—to deliver an end-to-end solution for efficient meal planning and grocery shopping.  

## **Agents**  

### 1. **Dietary Analyst**  
**Role**: Nutritional Expert  
**Goal**: Analyze dietary preferences and create a personalized nutritional profile.  
- **Inputs**:  
   - Dietary requirements (e.g., vegetarian, gluten-free)  
   - Ingredients provided by the user  
   - Health goals (e.g., weight loss, muscle gain)  

- **Tasks**:  
   - Assess macronutrient and micronutrient needs (carbs, proteins, fats, vitamins).  
   - Identify dietary constraints and health considerations.  
   - Generate a detailed nutritional guideline.  

- **Output Deliverables**:  
   - Nutritional Profile Report  
   - Dietary Constraints Matrix  

---

### 2. **Menu Planner**  
**Role**: Culinary Strategist  
**Goal**: Create a diverse, nutritionally balanced weekly meal plan with recipes.  
- **Inputs**:  
   - Nutritional Profile and constraints from the Dietary Analyst  
   - User-provided ingredients and preferences  

- **Tasks**:  
   - Develop a 7-day meal plan (3 meals/day).  
   - Create recipes with ingredients, cuisine types, preparation steps, and nutrition breakdowns.  
   - Ensure ingredient reuse and variety.  

- **Output Deliverables**:  
   - Comprehensive Weekly Menu Plan  
   - Recipe Collection (detailed with calories and nutrients)  
   - Nutritional Breakdown Document  

---

### 3. **Shopping List Optimizer**  
**Role**: Procurement Strategist  
**Goal**: Convert the meal plan into an efficient, categorized, and cost-optimized shopping list.  
- **Inputs**:  
   - Weekly menu and recipes from the Menu Planner  

- **Tasks**:  
   - Aggregate ingredients and estimate quantities.  
   - Categorize items (e.g., produce, proteins, pantry staples).  
   - Suggest cost-effective substitutions.  
   - Optimize for budget and minimal food waste.  

- **Output Deliverables**:  
   - Categorized Shopping List  
   - Ingredient Quantity Worksheet  
   - Cost Estimation Report  

---

## **Workflow**  
1. **Dietary Analyst**: Analyzes user preferences and health goals to generate a nutritional profile.  
2. **Menu Planner**: Designs a 7-day meal plan with detailed recipes and nutritional breakdowns.  
3. **Shopping List Optimizer**: Converts the menu into a categorized shopping list with cost estimates.  
4. **Final Output**: A consolidated report including:  
   - Dietary Preference Report
   - Weekly Menu Plan
   - Shopping List  

---

## **Technology Stack**  
- **Framework**: CrewAI  
- **Language**: Python  


## **Example Input**  
```python
{
    'dietary_requirement': 'Gluten-Free',
    'ingredients': 'Chicken, Sweet Potatoes, Kale, Avocado, Blueberries',
    'health_goals': 'Support weight loss, improve gut health'
}
```  

---

## **Potential Enhancements**  
- Machine learning for personalized preference adaptation.  
- Integration with local grocery store APIs for real-time pricing.  
- Seasonal ingredient recommendations.  
- Dynamic adjustments for portion sizes and servings.  

---

## **Limitations**  
- Requires detailed user input for accurate results.  
- Relies on the trained data.  

---

## **Contributing**  
Contributions are welcome! To propose changes:  
1. Fork the repository.  
2. Create a new branch (`feature/your-feature`).  
3. Commit changes and open a pull request.  

---

## **License**  
This project is licensed under the **MIT License**.  

---

## **Contact**  
For questions or support, contact:  
- **Developer**: Cynthia Widjaja  
- **Email**: cynthia.widjaja@cstu.edu  
- **GitHub**: https://github.com/c1n5/my-planner/  


#Notes from CrewAI:
Welcome to the MyPlanner Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/my_planner/config/agents.yaml` to define your agents
- Modify `src/my_planner/config/tasks.yaml` to define your tasks
- Modify `src/my_planner/crew.py` to add your own logic, tools and specific args
- Modify `src/my_planner/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the my-planner Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The my-planner Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the MyPlanner Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
