import bpy

from collections import defaultdict


rna_listeners = defaultdict(dict)

def subscribe_to_rna_change(bpy_rna_type: type, attr_name: str, persistent: bool = False):
    def decorator(decorated_func):
        def rna_callback_decorator(decorated_func):
            def wrapper(*args, **kwargs):
                # print(f"RNA change {bpy_rna_type.__name__}.{attr_name}")
                ctx = bpy.context
                type_instance = getattr(ctx, bpy_rna_type.__name__.lower(), None)
                decorated_func(ctx, type_instance, getattr(type_instance, attr_name) if type_instance is not None else None)
            return wrapper

        owner = object()
        rna_listeners[bpy_rna_type][attr_name] = owner
        options = set()
        if persistent:
            options.add('PERSISTENT')
        bpy.msgbus.subscribe_rna(
            key=(bpy_rna_type, attr_name),
            owner=owner,
            args=(),
            notify=rna_callback_decorator(decorated_func),
            options=options
        )
        # return wrapper
    return decorator    


def register():
    if not rna_listeners:
        return
    print("\n-----------------------\nRNA Subscriptions:")
    for type, subscriptions in rna_listeners.items():
        print("\t> Type:", type.__name__)
        for attr in subscriptions.keys():
            print("\t\t.", attr)
    print("-----------------------")


def unregister():
    for type, subscriptions in rna_listeners.items():
        for owner in subscriptions.values():
            bpy.msgbus.clear_by_owner(owner)
