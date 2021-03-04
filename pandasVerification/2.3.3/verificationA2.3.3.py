# 連続値のカウントを行うソースコード
import pandas as pd
import random


def chk_dataframe_series(df):  # 比較するソースコード
    y = df['group1', 'group2']
    df['new'] = y.groupby((y != y.shift()).cumsum()).cumcount() + 1


if __name__ == '__main__':

    repeat_time = 10  # 繰り返す回数
    cum_execute_time = 0  # 累計処理時間
    dataframe_len = 100  # Dataframeのindexの長さ

    # データ作成
    random.seed(0)
    group1_list = [random.randint(0, 10) for j in range(dataframe_len)]
    random.seed(1)
    group2_list = [random.randint(0, 10) for j in range(dataframe_len)]
    random.seed(2)
    value_list = [random.randint(0, 10) for j in range(dataframe_len)]
    sample_df = pd.DataFrame({'group1': group1_list,
                              'group2': group2_list,
                              'value': value_list})

    chk_dataframe_series(sample_df)

    print('execute complete')
