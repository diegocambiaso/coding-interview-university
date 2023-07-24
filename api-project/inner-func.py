def has_permission(page):
    def permission(username):
        if username.lower() == "admin":
            return f"'{username}' has access to {page}."
        else:
            return f"'{username}' doesn't have access to {page}."
    return permission


check_admin_page_permision = has_permission("Admin Page")
print(type(check_admin_page_permision))

print(check_admin_page_permision("Admin"))

print(check_admin_page_permision("john"))