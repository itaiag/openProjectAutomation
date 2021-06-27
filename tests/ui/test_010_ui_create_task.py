from datetime import datetime

from main_config import config
from tests.ui.ui_common import do_ui_login


def test_010_ui_create_task():

    # Step 1 - Login to OpenProject
    home_page = do_ui_login(config["ui_login"]["username"], config["ui_login"]["password"])

    # Step 2 - On “Home” page, click “Select a project“ menu button, and select “TestProject1” from the drop-down
    project_name = "TestProject1"
    project_overview_page = home_page.select_project(project_name)

    # Step 3 - On “Project Overview” page, “Work packages”.
    # Once on the “Work packages” page, note the number of rows displayed in the work packages table.
    work_packages_page = project_overview_page.click_work_packages_link()
    initial_number_of_workpackages = work_packages_page.get_number_of_table_rows()

    # Step 4 - Click “+ Create” green button and select “TASK”
    new_work_package_page = work_packages_page.select_create_task()

    # Step 5 - Verify the text “New TASK” title on the form that got opened on the right side
    workpackage_type = new_work_package_page.get_work_package_type_button_text()
    assert workpackage_type == "TASK", "Displayed work package should be 'TASK'"

    # Step 6 - Type unique strings into the subject and description boxes
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    task_subject = f"Auto Task {timestamp}"
    task_description = f" This work package was created by an automated test @ {timestamp}"

    new_work_package_page\
        .write_subject(task_subject)\
        .write_description(task_description)

    # Step 7 - Click “Save” button
    work_packages_page = new_work_package_page.click_save_button()

    # Step 8 - Verify that a new row was added to the work packages table
    current_number_of_workpackages = work_packages_page.get_number_of_table_rows()
    assert current_number_of_workpackages == initial_number_of_workpackages + 1, f"Expected number of work packages: {initial_number_of_workpackages + 1}"

    # Step 9 - Verify the subject and type of the last table row
    row_dict = work_packages_page.read_table_row(current_number_of_workpackages-1)
    assert row_dict["subject"] == task_subject, f"Subjet in last table row should be '{task_subject}'"
    assert row_dict["type"] == "TASK", f"Type in last table row should be 'TASK'"
