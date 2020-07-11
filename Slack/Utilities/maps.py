Maps = {
    "Api.test": """{{
        "error": {error},
        "foo": {foo}
    }}""",
    "Calls.add": """{{
        "external_unique_id": {external_unique_id},
        "join_url": {join_url},
        "created_by": {created_by},
        "date_start": {date_start},
        "desktop_app_join_url": {desktop_app_join_url},
        "external_display_id": {external_display_id},
        "title": {title},
        "users": {users}
    }}""",
    "Calls.end": """{{
        "id": {id},
        "duration": {duration}
    }}""",
    "Calls.info": """{{
        "id": {id}
    }}""",
    "Calls.update": """{{
        "id": {id},
        "desktop_app_join_url": {desktop_app_join_url},
        "join_url": {join_url},
        "title": {title}
    }}""",
    "Calls.participants.add": """{{
        "id": {id},
        "users": {users}
    }}""",
    "Calls.participants.remove": """{{
        "id": {id},
        "users": {users}
    }}""",
    "Chat.delete": """{{
        "channel": {channel},
        "ts": {ts},
        "as_user": {as_user}
    }}""",
    "Chat.delete_scheduled_message": """{{
        "channel": {channel},
        "scheduled_message_id": {scheduled_message_id},
        "as_user": {as_user}
    }}""",
    "Chat.me_message": """{{
        "channel": {channel},
        "text": {text}
    }}""",
    "Chat.post_ephemeral": """{{
        "channel": {channel},
        "text": {text},
        "user": {user},
        "attachments": {attachments},
        "as_user": {as_user},
        "blocks": {blocks},
        "icon_emoji": {icon_emoji},
        "icon_url": {icon_url},
        "link_names": {link_names},
        "parse,": {parse,},
        "thread_ts": {thread_ts},
        "username": {username}
    }}""",
    "Chat.post_message": """{{
        "channel": {channel},
        "text": {text},
        "as_user": {as_user},
        "attachments": {attachments},
        "blocks": {blocks},
        "icon_emoji": {icon_emoji},
        "icon_url": {icon_url},
        "link_names": {link_names},
        "mrkdwn": {mrkdwn},
        "parse,": {parse},
        "reply_broadcast": {reply_broadcast},
        "thread_ts": {thread_ts},
        "unfurl_links": {unfurl_links},
        "unfurl_media": {unfurl_media},
        "username": {username}
    }}""",
    "Chat.schedule_message": """{{
        "channel": {channel},
        "post_at": {post_at},
        "text": {text},
        "as_user": {as_user},
        "attachments": {attachments},
        "blocks": {blocks},
        "link_names": {link_names},
        "parse,": {parse},
        "reply_broadcast": {reply_broadcast},
        "thread_ts": {thread_ts},
        "unfurl_links": {unfurl_links},
        "unfurl_media": {unfurl_media}
    }}""",
    "Chat.unfurl": """{{
        "channel": {channel},
        "text": {text},
        "ts": {ts},
        "unfurls": {unfurls},
        "user_auth_message": {user_auth_message},
        "user_auth_required": {user_auth_required},
        "user_auth_url": {user_auth_url},
    }}""",
    "Chat.update": """{{
        "channel": {channel},
        "ts": {ts},
        "as_user": {as_user},
        "attachments": {attachments},
        "blocks": {blocks},
        "link_names": {link_names},
        "parse,": {parse},
        "text": {text},
    }}""",
    "Conversations.archive": """{{
        "channel": {channel}
    }}""",
    "Conversations.close": """{{
        "channel": {channel}
    }}""",
    "Conversations.create": """{{
        "name": {name},
        "is_private": {is_private},
        "user_ids": {user_ids}
    }}""",
    "Conversations.invite": """{{
        "channel": {channel},
        "users": {users}
    }}""",
    "Conversations.join": """{{
        "channel": {channel}
    }}""",
    "Conversations.kick": """{{
        "channel": {channel},
        "user": {user}
    }}""",
    "Conversations.leave": """{{
        "channel": {channel}
    }}""",
    "Conversations.open": """{{
        "channel": {channel},
        "return_im": {return_im},
        "users": {users}
    }}""",
    "Conversations.rename": """{{
        "channel": {channel},
        "name": {name}
    }}""",
    "Conversations.set_purpose": """{{
        "channel": {channel},
        "purpose": {purpose}
    }}""",
    "Conversations.set_topic": """{{
        "channel": {channel},
        "topic": {topic}
    }}""",
    "Conversations.unarchive": """{{
        "channel": {channel}
    }}""",
    "Dialog.open": """{{
        "dialog": {dialog},
        "trigger_id": {trigger_id}
    }}""",
    "Files.delete": """{{
        "file": {file}
    }}""",
    "Files.revoke_public_url": """{{
        "file": {file}
    }}""",
    "Files.shared_public_url": """{{
        "file": {file}
    }}""",
    "Files.upload": """{{
        "channels": {channels},
        "content": {content},
        "filename": {filename},
        "filetype": {filetype},
        "initial_comment": {initial_comment},
        "thread_ts": {thread_ts}
    }}""",
    "Files.comments.delete": """{{
        "file": {file},
        "id": {id}
    }}""",
    "OAuth.access": """{{
        "code": {code},
        "client_id": {client_id},
        "client_secrete": {client_secret},
        "redirect_uri": {redirect_uri}
    }}""",
    "Pins.add": """{{
        "channel": {channel},
        "timestamp": {timestamp}
    }}""",
    "Pins.remove": """{{
        "channel": {channel},
        "file": {file},
        "file_comment": {file_comment},
        "timestamp": {timestamp}
    }}""",
    "Reactions.add": """{{
        "channel": {channel},
        "name": {name},
        "timestamp": {timestamp}
    }}""",
    "Reactions.remove": """{{
        "name": {name},
        "channel": {channel},
        "file": {file},
        "file_comment": {file_comment},
        "timestamp": {timestamp}
    }}""",
    "Reminder.add": """{{
        "text": {text},
        "time": {time},
        "user": {user}
    }}""",
    "Reminder.complete": """{{
        "reminder": {reminder}
    }}""",
    "Reminder.delete": """{{
        "reminder": {reminder}
    }}""",
    "Users.set_photo": """{{
        "crop_w": {crop_w},
        "crop_x": {crop_x},
        "crop_y": {crop_y}
    }}""",
    "Users.set_presence": """{{
        "presence": {presence}
    }}""",
    "Users.Profile.set": """{{
        "name": {name},
        "profile": {profile},
        "user": {user},
        "value": {value}
    }}""",
    "UserGroups.create": """{{
        "name": {name},
        "channels": {channels},
        "description": {description},
        "handle": {handle},
        "include_count": {include_count}
    }}""",
    "UserGroups.disable": """{{
        "usergroup": {usergroup},
        "include_count": {include_count}
    }}""",
    "UserGroups.enable": """{{
        "usergroup": {usergroup},
        "include_count": {include_count}
    }}""",
    "UserGroups.update": """{{
        "usergroup": {usergroup},
        "channels": {channels},
        "description": {description},
        "handle": {handle},
        "include_count": {include_count},
        "name": {name}
    }}""",
    "UserGroups.Users.update": """{{
        "usergroup": {usergroup},
        "users": {users},
        "include_count": {include_count}
    }}""",
    "Views.open": """{{
        "trigger_id": {trigger_id},
        "view": {view}
    }}""",
    "Views.publish": """{{
        "user_id": {user_id},
        "view": {view},
        "hash": {hash}
    }}""",
    "Views.push": """{{
        "trigger_id": {trigger_id},
        "view": {view}
    }}""",
    "Views.update": """{{
        "view": {view},
        "external_id": {external_id},
        "hash": {hash},
        "view_id": {view_id}
    }}"""
}
