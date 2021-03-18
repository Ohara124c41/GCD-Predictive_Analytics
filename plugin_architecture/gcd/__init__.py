import pluggy

hookimpl = pluggy.HookimplMarker("gcd")
"""Marker to be imported and used in plugins (and for own implementations)"""
