# Copyright (C) 2013-2015 Samuel Damashek, Peter Foley, James Forcier, Srijay Kasturi, Reed Koser, Christopher Reffett, and Fox Wilson
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

from sqlalchemy import func
from ..helpers.command import Command
from ..helpers.orm import Log


@Command('rquote', ['db', 'target'])
def cmd(send, msg, args):
    """Returns a random quote from $nick.
    Syntax: {command} <nick>
    """
    quote = args['db'].query(Log.msg, Log.source)
    if msg:
        quote = quote.filter(Log.source == msg, Log.target == args['target'])
    else:
        quote = quote.filter(Log.target == args['target'])
    quote = quote.order_by(func.random()).first()
    if quote and msg:
        send(quote.msg)
    elif quote:
        send("%s -- %s" % quote)
    elif msg:
        send("%s isn't very quotable." % msg)
    else:
        send("Nobody is very quotable :(")