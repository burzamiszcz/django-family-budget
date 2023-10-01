# django-family-budget
A project made for recruitment purposes. Due to the voluminousness of the task and lack of time, I decided to limit myself to selected functionalities. I skipped logging and registration (I think this is the basis of the basics), expenses and income do not have categories, deletion I implemented only for budget sharing, implemented one test (I think in recruitment tasks it is a matter of understanding how tests work, here you could write MANY of them) and maybe something else I did not mention.

Below I described the installation process and existing endpoints


### Getting Started
To set up and run the Django Family Budget, follow the steps below:

1. Clone the repository:
```bash
git clone https://github.com/burzamiszcz/django-family-budget.git
```
2. Go to the app folder
```bash
cd family_budget_project
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
5. Make migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Make migrations:
```bash
python manage.py loaddata fixtures/initial_data.json
```
6. Run server:
```bash
python manage.py runserver
```

## Project Structure
1. **Budgets List and Creation**
   - Path: `/budgets/`
   - Description: This path leads to a view that displays a list of existing budgets and allows users to create new ones.
   - Methods: GET (to retrieve the list of budgets), POST (to create a new budget)
   - Example: `GET /budgets/`

2. **Budget Details**
   - Path: `/budgets/<int:pk>`
   - Description: This path leads to a view that displays detailed information about a specific budget based on its identifier (pk).
   - Method: GET (to retrieve the details of the budget)
   - Example: `GET /budgets/1`

3. **Income Creation**
   - Path: `/budgets/<int:pk>/incomes/create/`
   - Description: This path leads to a view that allows users to add new income entries to a specific budget.
   - Method: POST (to create a new income entry)
   - Example: `POST /budgets/1/incomes/create/`

4. **Expense Creation**
   - Path: `/budgets/<int:pk>/expenses/create/`
   - Description: This path leads to a view that allows users to add new expense entries to a specific budget.
   - Method: POST (to create a new expense entry)
   - Example: `POST /budgets/1/expenses/create/`

5. **Share Budget Update**
   - Path: `/budgets/<int:pk>/share/update`
   - Description: This path leads to a view that allows users to update the list of users with whom a specific budget is shared.
   - Method: PUT (to update the list of shared users)
   - Example: `PUT /budgets/1/share/update`

6. **Share Budget Delete**
   - Path: `/budgets/<int:pk>/share/delete`
   - Description: This path leads to a view that allows users to remove specific users from the shared list of a budget.
   - Method: DELETE (to remove shared users)
   - Example: `DELETE /budgets/1/share/delete`
