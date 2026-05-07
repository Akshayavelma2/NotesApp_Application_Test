def should_rerun(error_message):
#flaky_errors means errors are not Consistent and rerun
    flaky_errors = [
        "stale element reference",
        "element click intercepted",
        "timeout",
        "no such element"
    ]

    error_message = error_message.lower()

    for error in flaky_errors:
        if error in error_message:
            return True

    return False