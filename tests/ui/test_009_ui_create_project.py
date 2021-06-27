from datetime import datetime

from main_config import config
from tests.ui.ui_common import do_ui_login


def test_009_ui_create_project():

    project_name = f"Auto Project {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

    # Step 1 - Login to OpenProject
    home_page = do_ui_login(config["ui_login"]["username"], config["ui_login"]["password"])

    # Step 2 - On “Home” page, click “ + Project “ green button
    new_project_page = home_page.click_new_project_button()

    # Step 3 - On “New project” page, type a unique value for the project name.
    # Step 4 - Click “ADVANCED SETTINGS” title
    # Step 5 - Type some text to the description text box
    new_project_page\
        .write_project_name(project_name)\
        .click_advanced_settings_title()\
        .write_description(" This project was created by an automated test")

    # Step 6 - Verify the value of the “Identifier” field
    project_identifier = new_project_page.get_project_identifier()
    expected_project_identifier = project_name.lower().replace(" ", "-").replace("/", "-").replace(":", "-")
    assert expected_project_identifier == project_identifier, f"Project identifier should be {expected_project_identifier}"

    # Step 7 - Select status “On track”
    new_project_page.select_status("On track")

    # Step 8 - Click “Create”
    work_packages_page = new_project_page.click_create_button()

    # Step 9 - On “Work packages” page, top left corner: verify the text on the button
    title = work_packages_page.get_project_menu_title()
    assert title == project_name, f"Projects menu title on 'Work Packages' page should be '{project_name}'"

