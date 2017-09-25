import pandas as pd

from biglearning.module2.common.data import DataSource, Outputs
import biglearning.module2.common.interface as I


# 是否自动缓存结果
bigquant_cacheable = True

# 如果模块已经不推荐使用，设置这个值为推荐使用的版本或者模块名，比如 v2
# bigquant_deprecated = '请更新到 ${MODULE_NAME} 最新版本'
bigquant_deprecated = None

# 模块是否外部可见，对外的模块应该设置为True
bigquant_public = True

# 是否开源
bigquant_opensource = True
bigquant_author = 'BigQuant'

# 模块接口定义
bigquant_category = '示例模块'
bigquant_friendly_name = 'Hello BigQuant Module'
bigquant_doc_url = 'https://bigquant.com/docs/'


def bigquant_run(
    input_ds: I.port('一个数据输入'),                 # 使用python anotation定义输入端
    another_input_ds: I.port('另一个数据输入'),
    param1: I.int('没有限制的int参数'),            # 使用python anotation定义参数
    param2: I.int('一个int参数', 0, 100),
    param3: I.float('一个float参数', min=-100.21, max=10),
    param5: I.choice('choice参数', ['hello', 'world', 'bigquant']),
    foo: I.code('文本字段'),
    param7: I.bool('bool参数，无默认值'),
    bar: I.code('简单python对象', I.code_python) = '[1, 2, 3, 4]',
    bar1: I.code('另一个python对象', I.code_python) = 'bigquant_run = [1, 2, 3]',
    bar2: I.code('python函数', I.code_python) = 'def bigquant_run(some_ds):\n    return Outputs(data=some_ds)',
    param6: I.bool('bool参数') = True,
    strparam: I.str('str参数') = 'some_default_value') -> [
        I.port('一个输出数据', 'some_ds'),            # 使用python anotation定义输出端
        I.port('另一个输出数据', 'another_ds', True),  # 可选输出端
    ]:
    '''
    这是一个示例模块，用来展示如何创建一个模块。您可以拷贝此模块并修改成你需要的模块。
    一个模块应该至少包括一个 bigquant_run 函数。
    '''
    # do something here ...
    df = pd.DataFrame({'a': [1, 2, 3, 4]})
    return Outputs(
        some_ds=DataSource.write_df(df),
        another_ds=DataSource.write_df(df),
    )


def bigquant_postrun(outputs):
    '''
    bigquant_postrun 后处理函数，可选。输入是主函数的输出，可以在这里对数据做处理，或者返回更友好的outputs数据格式。此函数输出不会被缓存。
    :param outputs: 输入数据
    :return: 返回后处理后的数据
    @opensource
    '''
    def read_some(self):
        return pd.read_hdf(self.some_ds.path, 'data')
    outputs.extend_methods(read_some=read_some)

    def plot_datatable(self, df, output="display"):
        from bigcharts.datatale import plot
        return plot(df, output)
    outputs.extend_methods(plot_datatable=plot_datatable)

    def plot_tabs(self, kvs, output="display"):
        from bigcharts.tabs import plot
        return plot(kvs, output)
    outputs.extend_methods(plot_tabs=plot_tabs)

    return outputs


if __name__ == '__main__':
    # 测试代码
    pass
