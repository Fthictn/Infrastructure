from typing import NamedTuple


class InternalSettings(NamedTuple):
    indexAwareRebalanceDisabled: bool
    rebalanceIndexWaitingDisabled: bool
    rebalanceIndexPausingDisabled: bool
    rebalanceIgnoreViewCompactions: bool
    rebalanceMovesPerNode: int
    rebalanceMovesBeforeCompaction: int
    maxParallelIndexers: int
    maxParallelReplicaIndexers: int
    maxBucketCount: int
    gotraceback: str
    indexAutoFailoverDisabled: bool
    certUseSha1: bool

    def set_indexAwareRebalanceDisabled(self, indexAwareRebalanceDisabled):
        self.indexAwareRebalanceDisabled = indexAwareRebalanceDisabled

    def set_rebalanceIndexWaitingDisabled(self, rebalanceIndexWaitingDisabled):
        self.rebalanceIndexWaitingDisabled = rebalanceIndexWaitingDisabled

    def set_rebalanceIndexPausingDisabled(self, rebalanceIndexPausingDisabled):
        self.rebalanceIndexPausingDisabled = rebalanceIndexPausingDisabled

    def set_rebalanceIgnoreViewCompactions(self, rebalanceIgnoreViewCompactions):
        self.rebalanceIgnoreViewCompactions = rebalanceIgnoreViewCompactions

    def set_rebalanceMovesPerNode(self, rebalanceMovesPerNode):
        self.rebalanceMovesPerNode = rebalanceMovesPerNode

    def set_rebalanceMovesBeforeCompaction(self, rebalanceMovesBeforeCompaction):
        self.rebalanceMovesBeforeCompaction = rebalanceMovesBeforeCompaction

    def set_maxParallelIndexers(self, maxParallelIndexers):
        self.maxParallelIndexers = maxParallelIndexers

    def set_maxParallelReplicaIndexers(self, maxParallelReplicaIndexers):
        self.maxParallelReplicaIndexers = maxParallelReplicaIndexers

    def set_maxBucketCount(self, maxBucketCount):
        self.maxBucketCount = maxBucketCount

    def set_gotraceback(self, gotraceback):
        self.gotraceback = gotraceback

    def set_indexAutoFailoverDisabled(self, indexAutoFailoverDisabled):
        self.indexAutoFailoverDisabled = indexAutoFailoverDisabled

    def set_certUseSha1(self, certUseSha1):
        self.certUseSha1 = certUseSha1

    def get_indexAwareRebalanceDisabled(self):
        return self.indexAwareRebalanceDisabled

    def get_rebalanceIndexWaitingDisabled(self):
        return self.rebalanceIndexWaitingDisabled

    def get_rebalanceIndexPausingDisabled(self):
        return self.rebalanceIndexPausingDisabled

    def get_rebalanceIgnoreViewCompactions(self):
        return self.rebalanceIgnoreViewCompactions

    def get_rebalanceMovesPerNode(self):
        return self.rebalanceMovesPerNode

    def get_rebalanceMovesBeforeCompaction(self):
        return self.rebalanceMovesBeforeCompaction

    def get_maxParallelIndexers(self):
        return self.maxParallelIndexers

    def get_maxParallelReplicaIndexers(self):
        return self.maxParallelReplicaIndexers

    def get_maxBucketCount(self):
        return self.maxBucketCount

    def get_gotraceback(self):
        return self.gotraceback

    def get_indexAutoFailoverDisabled(self):
        return self.indexAutoFailoverDisabled

    def get_certUseSha1(self):
        return self.certUseSha1
