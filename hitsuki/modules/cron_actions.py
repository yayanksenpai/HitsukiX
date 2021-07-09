# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2021 HitaloSama.
#
# This file is part of Hitsuki (Telegram Bot)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import aiocron

from hitsuki.modules.owner_stuff import do_backup
from hitsuki.config import get_bool_key, get_int_key


@aiocron.crontab('0 * * * *')
async def backup():
    if get_bool_key("AUTO_BACKUP") is False:
        return
    channel_id = get_int_key("LOGS_CHANNEL_ID")
    await do_backup(channel_id)
