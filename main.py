from pyscript import document


def candidate_checker(e=None):
    club_members = [
        "youngeun song",
        "jacob opilla",
        "athena silva",
        "ila martinez",
        "sophie gamban"
    ]

    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()

    result = document.getElementById("result")

    if not f_name or not l_name:
        result.textContent = "Please enter both your first and last name!"
        result.className = "result error"
        result.hidden = False
        return

    candidate = f"{f_name} {l_name}"

    candidate = candidate.lower()

    member_checker = candidate in club_members

    if member_checker:
        message = (
            f"Congratulations {f_name.strip().title()} "
            f"{l_name.strip().title()}, "
            "you are singing onto Glee Club!! :D"
        )
        result.className = "result success"
    else:
        message = (
            f"Sorry {f_name.strip().title()} "
            f"{l_name.strip().title()}, "
            "your name is not on list..!! TnT"
        )
        result.className = "result error"

    result.textContent = message
    result.hidden = False
