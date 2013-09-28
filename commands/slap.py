# Copyright (C) 2013 Fox Wilson, Peter Foley, Srijay Kasturi, Samuel Damashek, James Forcier and Reed Koser
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from random import choice
from helpers.command import Command


@Command('slap', ['channels', 'target', 'config'])
def cmd(send, msg, args):
    """Slap somebody.
    Syntax: !slap <nick> for <reason>
    """
    implements = ['a large trout', 'a clue-by-four', 'a fresh haddock', 'moon', 'an Itanium', 'fwilson', 'a wombat']
    methods = ['around a bit', 'upside the head']
    if not msg:
        channel = args['target'] if args['target'] != 'private' else args['config']['core']['channel']
        users = list(args['channels'][channel].users())
        slap = 'slaps %s %s with %s'
        send(slap % (choice(users), choice(methods), choice(implements)), 'action')
    else:
        reason = ''
        method = choice(methods)
        implement = ''
        msg = msg.split()
        slapee = msg[0]
        #Basic and stupid NLP!
        i = 1
        while i < len(msg):
            if msg[i] == 'for':
                if reason != '':
                    send("BAD! You can only have one for clause!")
                    return
                i += 1
                while i < len(msg):
                    if msg[i] == 'with':
                        break
                    reason += " "
                    reason += msg[i]
                    i += 1
                reason = reason.strip()
            elif msg[i] == 'with':
                if implement != '':
                    send("BAD! You can only have one with clause!")
                    return
                i += 1
                while i < len(msg):
                    if msg[i] == 'for':
                        break
                    implement += msg[i]
                    implement += ' '
                    i += 1
                implement = implement.strip()

        if implement == '':
            implement = choice(implements)
        slap = 'derp lol'
        if reason != '':
            slap = 'slaps %s %s with %s for %s' % (slapee, method, implement, reason)
        else:
            slap = 'slaps %s %s with %s' % (slapee, method, implement)
        send(slap, 'action')
        #if "for" in msg:
        #    msg = msg.split("for")
        #    slap = slap % (msg[0].strip(), choice(methods), choice(implements) + " for" + msg[1])
        #else:
        #    slap = slap % (msg, choice(methods), choice(implements))
        #send(slap, 'action')
