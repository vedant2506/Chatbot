# Temporary conversation memory. Cleared on /start, cancel, and success.

drafts = {}
search_state = {}
edit_state = {}
contact_mode = {}
flag_state = {}
admin_state = {}
announce_state = {}
notif_state = {}


def clear_user(chat_id):
    drafts.pop(chat_id, None)
    search_state.pop(chat_id, None)
    edit_state.pop(chat_id, None)
    contact_mode.pop(chat_id, None)
    flag_state.pop(chat_id, None)
    admin_state.pop(chat_id, None)
    announce_state.pop(chat_id, None)
    notif_state.pop(chat_id, None)
