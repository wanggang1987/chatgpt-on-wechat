"""
channel factory
"""

def create_channel(channel_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    if channel_type == 'itchat':
        from channel.wechat.itchat_channel import WechatChannel
        return WechatChannel()
    elif channel_type == 'wechaty':
        from channel.wechat.wechaty_channel import WechatyChannel
        return WechatyChannel()
    raise RuntimeError
