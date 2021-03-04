# データの連続判定を行うソースコード
import pandas as pd
import random
from memory_profiler import profile


@profile  # メモリ使用量検証用
def chk_dataframe_series(df):  # 比較するソースコード
    sorted_df = df.drop_duplicates(subset=['group', 'value']).sort_values(['group', 'value'])
    created_df = sorted_df[(sorted_df.group != sorted_df.group.shift()) & (sorted_df.value.diff() != 1)]


if __name__ == '__main__':

    repeat_time = 10  # 繰り返す回数
    cum_execute_time = 0  # 累計処理時間
    dataframe_len = 10000  # Dataframeのindexの長さ

    # データ作成
    random.seed(0)
    group_list = [random.randint(0, 10) for j in range(dataframe_len)]
    random.seed(1)
    value_list = [random.randint(0, 10) for j in range(dataframe_len)]
    sample_df = pd.DataFrame({'group': group_list,
                              'value': value_list})

    chk_dataframe_series(sample_df)
