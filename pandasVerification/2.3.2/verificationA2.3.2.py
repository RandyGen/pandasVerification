# 連続値のカウントを行うソースコード
import pandas as pd
import random
from memory_profiler import profile


@profile  # メモリ使用量検証用
def chk_dataframe_series(df):  # 比較するソースコード
    y = df['group']
    df['new'] = y.groupby((y != y.shift()).cumsum()).cumcount() + 1


if __name__ == '__main__':

    repeat_time = 10  # 繰り返す回数
    cum_execute_time = 0  # 累計処理時間
    dataframe_len = 1000  # Dataframeのindexの長さ

    # データ作成
    random.seed(0)
    group_list = [random.randint(0, 10) for j in range(dataframe_len)]
    random.seed(1)
    value_list = [random.randint(0, 10) for j in range(dataframe_len)]
    sample_df = pd.DataFrame({'group': group_list,
                              'value': value_list})

    chk_dataframe_series(sample_df)
