# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, ctypes_byte_str, c_bool32)
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    Edge, Timescale, TriggerType)


class ArmStartTrigger(object):
    """
    Represents the arm start trigger configurations for a DAQmx task.
    """
    def __init__(self, task_handle):
        self._handle = task_handle

    @property
    def dig_edge_dig_fltr_enable(self):
        """
        bool: Specifies whether to apply the pulse width filter to the
            signal.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeArmStartTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_enable.setter
    def dig_edge_dig_fltr_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeArmStartTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_enable.deleter
    def dig_edge_dig_fltr_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeArmStartTrigDigFltrEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_min_pulse_width(self):
        """
        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_min_pulse_width.setter
    def dig_edge_dig_fltr_min_pulse_width(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeArmStartTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_min_pulse_width.deleter
    def dig_edge_dig_fltr_min_pulse_width(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeArmStartTrigDigFltrMinPulseWidth)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_timebase_rate(self):
        """
        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        """
        val = ctypes.c_double()

        cfunc = (lib_importer.windll.
                 DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_fltr_timebase_rate.setter
    def dig_edge_dig_fltr_timebase_rate(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_timebase_rate.deleter
    def dig_edge_dig_fltr_timebase_rate(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseRate)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_fltr_timebase_src(self):
        """
        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @dig_edge_dig_fltr_timebase_src.setter
    def dig_edge_dig_fltr_timebase_src(self, val):
        cfunc = (lib_importer.windll.
                 DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_fltr_timebase_src.deleter
    def dig_edge_dig_fltr_timebase_src(self):
        cfunc = (lib_importer.windll.
                 DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseSrc)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_dig_sync_enable(self):
        """
        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeArmStartTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @dig_edge_dig_sync_enable.setter
    def dig_edge_dig_sync_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeArmStartTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_dig_sync_enable.deleter
    def dig_edge_dig_sync_enable(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeArmStartTrigDigSyncEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_edge(self):
        """
        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital signal to arm the task for a Start Trigger.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetDigEdgeArmStartTrigEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Edge(val.value)

    @dig_edge_edge.setter
    def dig_edge_edge(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetDigEdgeArmStartTrigEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_edge.deleter
    def dig_edge_edge(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeArmStartTrigEdge
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def dig_edge_src(self):
        """
        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Arm Start Trigger.
        """
        cfunc = lib_importer.windll.DAQmxGetDigEdgeArmStartTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @dig_edge_src.setter
    def dig_edge_src(self, val):
        cfunc = lib_importer.windll.DAQmxSetDigEdgeArmStartTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @dig_edge_src.deleter
    def dig_edge_src(self):
        cfunc = lib_importer.windll.DAQmxResetDigEdgeArmStartTrigSrc
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def term(self):
        """
        str: Indicates the name of the internal Arm Start Trigger
            terminal for the task. This property does not return the
            name of the trigger source terminal.
        """
        cfunc = lib_importer.windll.DAQmxGetArmStartTerm
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @property
    def time_timescale(self):
        """
        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for timestamps used in an arm start time trigger.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetArmStartTrigTimescale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Timescale(val.value)

    @time_timescale.setter
    def time_timescale(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetArmStartTrigTimescale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @time_timescale.deleter
    def time_timescale(self):
        cfunc = lib_importer.windll.DAQmxResetArmStartTrigTimescale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def timestamp_enable(self):
        """
        bool: Specifies whether the arm start trigger timestamp is
            enabled. If the timestamp is enabled but no resources are
            available, an error will be returned at run time.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetArmStartTrigTimestampEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @timestamp_enable.setter
    def timestamp_enable(self, val):
        cfunc = lib_importer.windll.DAQmxSetArmStartTrigTimestampEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @timestamp_enable.deleter
    def timestamp_enable(self):
        cfunc = lib_importer.windll.DAQmxResetArmStartTrigTimestampEnable
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def timestamp_timescale(self):
        """
        :class:`nidaqmx.constants.Timescale`: Specifies the arm start
            trigger timestamp timescale.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetArmStartTrigTimestampTimescale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return Timescale(val.value)

    @timestamp_timescale.setter
    def timestamp_timescale(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetArmStartTrigTimestampTimescale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @timestamp_timescale.deleter
    def timestamp_timescale(self):
        cfunc = lib_importer.windll.DAQmxResetArmStartTrigTimestampTimescale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def trig_type(self):
        """
        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to arm the task for a Start Trigger. If you
            configure an Arm Start Trigger, the task does not respond to
            a Start Trigger until the device receives the Arm Start
            Trigger.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetArmStartTrigType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return TriggerType(val.value)

    @trig_type.setter
    def trig_type(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetArmStartTrigType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @trig_type.deleter
    def trig_type(self):
        cfunc = lib_importer.windll.DAQmxResetArmStartTrigType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

