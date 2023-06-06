# Copyright (2023) Beijing Volcano Engine Technology Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Context:
    """
        Record the current runtime environment information.

    """
    def __init__(self):
        self.context = {}

    def set_context(self, key, val):
        self.context[key] = val

    def get_context(self, key):
        if self.context.get(key):
            return self.context[key]
        else:
            return None

    def construct_sensitivity_info(self):
        sensitivities = {}
        col_name = self.get_context("source_col_names")
        sensitivity = self.get_context("sensitivities")
        if len(col_name) == len(sensitivity):
            for i in range(len(col_name)):
                sensitivities[col_name[i]] = sensitivity[i]
        return sensitivities

    # format for debug info
    def construct_debug_info(self):
        debug_info = {
            'query_info':
            {
                "source_sql": self.get_context("source_sql"),
                "rewrited_sql": self.get_context("rewrited_sql"),
                "trace_id": self.get_context("trace_id"),
            },
            'method': self.get_context("noise_method"),
            'sensitivity': self.construct_sensitivity_info(),
            'profile': self.get_context("time_perf").get_cost()
        }
        return debug_info

    # format for dp-sql info
    def construct_dp_info(self):
        dp_info = {
            'privacy': self.get_context("accountant"),
            'utility': self.get_context("utility_dict_list")
        }
        return dp_info
"""
这是一个 Python 类，名为 Context。它可以帮助记录当前运行时环境的信息，并提供一些方法来处理这些信息。

在类的初始化函数 init 中，它创建了一个空字典 self.context 作为存储环境信息的容器。

接下来的 set_context 方法和 get_context 方法分别用于设置和获取环境信息中的特定键值对。如果指定的 key 存在于字典 self.context 中，则可以通过 get_context 方法获取其对应的 value 值；否则返回 None。

construct_sensitivity_info 方法是一个辅助方法，它通过读取环境变量 source_col_names 和 sensitivities，构造出一个敏感度字典 sensitivities。具体来说，source_col_names 存储了查询语句涉及到的列名列表，sensitivities 存储了这些列对应的敏感度列表。

construct_debug_info 方法用于构造 debug 信息，包括源查询语句、重写后的查询语句、追踪 ID、隐私保护方法等内容。其中，源查询语句、重写后的查询语句和追踪 ID 存储在查询信息字典 query_info 中，隐私保护方法存储在 method 中，敏感度信息则通过调用 construct_sensitivity_info 方法构造得到，时间性能则通过 time_perf 字典获取。

construct_dp_info 方法用于构造差分隐私信息，包括隐私相关参数和实用性参数。隐私参数存储在 accountant 中，实用性参数则存储在 utility_dict_list 中，并通过字典的形式返回。

总之，Context 类提供了一些方法来方便地处理和读取运行时环境信息，并且可以将这些信息组合成不同的数据结构，以满足不同的需求。
"""
